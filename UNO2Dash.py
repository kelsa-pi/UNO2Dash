# !/usr/bin/python3

import os
import sqlite3
from bs4 import BeautifulSoup

docset_name = 'UNO.docset'
docset_doc = 'UNO.docset/Contents/Resources/Documents'

docset_db = os.path.join(docset_name,'Contents', 'Resources','docSet.dsidx')
conn = sqlite3.connect(docset_db)
cur = conn.cursor()

try:
    cur.execute('DROP TABLE searchIndex;')
except:
    pass

cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

exclude = [
    'Main Page', 'Related Pages' 'Namespaces', 'Classes', 'Files', 'Class List',
    'Class Index', 'Class Hierarchy', 'Class Members', 'All', 'Functions',
    'Variables', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '',
    'Related\xa0Pages', 'Class\xa0Hierarchy', '']

pages_types = {
    'functions_func': 'Method',
    'functions_vars': 'Field',
    'namespacemembers_enum': 'Enum',
    'namespacemembers_vars': 'Variable',
    'namespacemembers_type': 'Type',
    'namespacemembers_eval': 'Constant',
    }

for root, dirs, files in os.walk(docset_doc, topdown=False):
    for f in files:
        if f.startswith('classes.html'):
            page = open(os.path.join(docset_doc, f)).read()
            soup = BeautifulSoup(page, 'html.parser')
            for tag in soup.find_all('td'):
                elements = tag.text.split(':')
                all_links = tag.find_all('a')
                try:
                    link = [(link.text, link.attrs['href']) for link in all_links]
                    types = 'Class'
                    for (name, path) in link:
                        if name not in exclude:
                            fullname = name
                            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (fullname, types, path))
                except:
                    pass
        else:
            for p in pages_types.keys():
                if f.startswith(p):
                    page = open(os.path.join(docset_doc, f)).read()
                    soup = BeautifulSoup(page, 'html.parser')
                    for tag in soup.find_all('li'):
                        elements = tag.text.split(':')
                        item = elements[0].replace('\n', '').replace('()', '')
                        all_links = tag.find_all('a')
                        link = [(link.text, link.attrs['href']) for link in all_links]
                        types = pages_types[p]
                        for (name, path) in link:
                            if name not in exclude:
                                fullname = name + '::' + item
                                cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (fullname, types, path))

conn.commit()
conn.close()

# add info.plist
plist_path = os.path.join(docset_name, "Contents", "Info.plist")
plist_cfg = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleIdentifier</key>
    <string>UNO</string>
    <key>CFBundleName</key>
    <string>UNO</string>
    <key>DocSetPlatformFamily</key>
    <string>UNO</string>
    <key>isDashDocset</key>
    <true/>
    <key>dashIndexFilePath</key>
    <string>index.html</string>
</dict>
</plist>
"""
with open(plist_path,'w') as pl:
    pl.write(plist_cfg)

print('\nFinished')


