# dev-solaris-valve
Tango Device Server for the valve device.

Shutter
=======
Tango device server for vacuum valves

What's inside
-------------
This repository contains installation files required to use Valve and FastValve
Tango Device Classes. 
 
How to install
--------------

First, clone git repository:
```console
git clone https://github.com/synchrotron-solaris/dev-solaris-valve.git
```
Then, enter the repository:
```console
cd dev-solaris-valve
```
Now you can use:
```console
python setup.py install
```
or:
```console
pip install .
```

How to run
----------
After installation, there are two scripts: `Valve` and `FastValve`.
You can use it via:
```console
Valve instance_name
```
or
```console
FastValve instance_name
```
Remember that Device Server instance has to registered in database previously.

Requirements
------------

- `setuptools`
- `facadedevice` >= 1.0.1
- `pytango` >= 9.2.1

License
-------
This sample project is distributed under LGPLv3 (see `LICENSE` file).
