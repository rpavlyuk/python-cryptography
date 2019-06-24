# python-cryptography
Python Cryptography RPM packaging for CentOS 7.x and Fedora 21+ versions.

The project itself is at: https://github.com/pyca/cryptography

## Usage

* Make sure you clone the project with submodules:
```bash
git clone --recurse-submodules https://github.com/rpavlyuk/python-cryptography.git && cd ./python-cryptography
```
* Building the RPM in quick-n-dirty way:
```bash
cd ./python-cryptography
make rpm
```
Search for lines beginning with `Wrote: ...` in the last 5-6 lines of log output -- this is where your RPM is. Run `yum install -y <path to RPM>` to have the file installed.

NOTE: You will have Fedora-ready RPM when running the build on Fedora and correspondingly you'll get EL7 version of RPM when running on CentOS. Beware that those packages are not intercompatible because of different dependecies.
