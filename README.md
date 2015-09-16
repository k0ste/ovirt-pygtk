# ovirt-pygtk
Run defined command via ovirt-engine-cli after auth as current user. Is used for connect to VM Spice console, usual.

Dependencies:
ovirt-engine-cli build with 'add_password_option.patch' (included), also available as [Arch Linux Package](https://aur.archlinux.org/packages/ovirt-engine-cli)

Checks:
* ~/.ovirtshellrc is present
* ovirt-engine-cli is installed (try import ovirtcli)
* command for run is defined

--domain only used for interface (for now).

Example:

```
/usr/bin/python2 ovirt-pygtk.py --command 'console nginx.balancer' --domain 'rhev'
```

After input password, remote-viewer should be opened console VM nginx.balancer.
