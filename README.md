UNO2Dash
=======================
**U**niversal **N**etwork **O**bjects (UNO) is the component model used in the OpenOffice.org and LibreOffice computer software application suites. Complete UNO language bindings exist for C++ (compiler-dependent), Java, Object REXX, Python (PyUNO), and Tcl. Bindings allowing access, but not writing, to components exist for StarOffice Basic, OLE Automation and the .NET Common Language Infrastructure.

**Dash** is offline documentation browser. Dash-like apps are:
* [Dash](https://kapeli.com/dash) for OS X,
* [Velocity]() for Windows, 
* [Zeal](https://zealdocs.org/) for Linux,
* [Dash](https://kapeli.com/dash_ios) for iOS and
* [LovelyDocs](http://lovelydocs.io) for Android.

IDE Plugins: Atom, Brackets, Emacs, KDevelop, PyCharm, Sublime Text, VIM, Visual Studio Code...

## Generate docset
Used UNO documentation from [LibreOffice](https://www.libreoffice.org). For general instructions see [Any HTML Documentation](https://kapeli.com/docsets#dashDocset).
1. Download and install the latest [LibreOffice SDK](https://www.libreoffice.org/download/download/)
1. Dowlnoad or clone this repo
1. Copy content of the SDK documentation folder `ref` (e.g. on Ubuntu `/opt/libreoffice5.3/sdk/docs/idl/ref`) to `UNO.docset/Contents/Resources/Documents/`folder (~ 300 MB) 
1. Run script `UNO2Dash.py`
1. Place `UNO.docset`in Dash-like apps path (e.g on Ubuntu `USER/.local/share/Zeal/Zeal/docsets/`)
