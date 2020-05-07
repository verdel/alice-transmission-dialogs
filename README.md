# alice-transmission-dialogs - Dialog for Yandex.Alice. Work with Transmission Torrent Client


What is this?
-------------
With transmission alice dialog you can get information from your Transmission torrent client by Yandex.Alice.


Installation
------------
on most UNIX-like systems, you'll probably need to run the following
`install` commands as root or by using sudo*

**from source**
```console
pip install git+http://github.com/verdel/alice-trasnmission-dialogs
```
**or**
```console
git clone git://github.com/verdel/alice-trasnmission-dialogs
cd alice-trasnmission-dialogs
python setup.py install
```

as a result, the ``alice_transmission`` executable will be installed into a system ``bin``
directory

Usage
-----
usage: alice_transmission [-h] [--tr-address string] [--tr-port string] [--tr-username string] [--tr-password string] [--debug]

Alice Transmission Dialog

optional arguments:
  -h, --help            show this help message and exit
  --tr-address string   Transmission client address
  --tr-port string      Transmission client port
  --tr-username string  Username for transmission client
  --tr-password string  Password for transmission client
  --debug               Enable debug level logging