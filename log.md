komichi@komichi-MacBookPro:~$ /sbin/lsmod 
.bash_logout               Music/
.bashrc                    Pictures/
.cache/                    .profile
.config/                   Public/
Desktop/                   snap/
Documents/                 .ssh/
Downloads/                 .sudo_as_admin_successful
.gitconfig                 Templates/
.gnupg/                    Videos/
.local/                    .viminfo
komichi@komichi-MacBookPro:~$ /sbin/lsmod | grep hci_usb
intel_xhci_usb_role_switch    12288  0
komichi@komichi-MacBookPro:~$ /sbin/lsmod | grep bluetooth
bluetooth            1028096  73 btrtl,btmtk,btqca,btintel,hci_uart,btbcm,bnep,btusb,rfcomm
ecdh_generic           16384  3 bluetooth
komichi@komichi-MacBookPro:~$ /usr/bin/hciconfig 
hci1:	Type: Primary  Bus: UART
	BD Address: F0:18:98:9C:37:A4  ACL MTU: 1021:8  SCO MTU: 192:1
	UP RUNNING 
	RX bytes:2038 acl:0 sco:0 events:130 errors:0
	TX bytes:8296 acl:0 sco:0 commands:130 errors:0

hci0:	Type: Primary  Bus: USB
	BD Address: 00:1B:DC:FE:DF:6E  ACL MTU: 310:10  SCO MTU: 64:8
	UP RUNNING 
	RX bytes:1462 acl:0 sco:0 events:111 errors:0
	TX bytes:8083 acl:0 sco:0 commands:111 errors:0

komichi@komichi-MacBookPro:~$ hciconfig 
hci1:	Type: Primary  Bus: UART
	BD Address: F0:18:98:9C:37:A4  ACL MTU: 1021:8  SCO MTU: 192:1
	UP RUNNING 
	RX bytes:2038 acl:0 sco:0 events:130 errors:0
	TX bytes:8296 acl:0 sco:0 commands:130 errors:0

hci0:	Type: Primary  Bus: USB
	BD Address: 00:1B:DC:FE:DF:6E  ACL MTU: 310:10  SCO MTU: 64:8
	UP RUNNING 
	RX bytes:1462 acl:0 sco:0 events:111 errors:0
	TX bytes:8083 acl:0 sco:0 commands:111 errors:0

komichi@komichi-MacBookPro:~$ hcitool scan
Scanning ...
	00:04:3E:84:12:00	OBDLink MX+ 93244
	41:42:DB:9B:D5:26	E-350BS
komichi@komichi-MacBookPro:~$ l2ping -c 4 00:04:3E:84:12:00
Can't create socket: Operation not permitted
komichi@komichi-MacBookPro:~$ sudo l2ping -c 4 00:04:3E:84:12:00
[sudo] password for komichi: 
Ping: 00:04:3E:84:12:00 from F0:18:98:9C:37:A4 (data size 44) ...
44 bytes from 00:04:3E:84:12:00 id 0 time 6.81ms
44 bytes from 00:04:3E:84:12:00 id 1 time 37.46ms
44 bytes from 00:04:3E:84:12:00 id 2 time 37.40ms
44 bytes from 00:04:3E:84:12:00 id 3 time 37.45ms
4 sent, 4 received, 0% loss
komichi@komichi-MacBookPro:~$ ^C
komichi@komichi-MacBookPro:~$ sdptool browse 00:04:3E:84:12:00
Browsing 00:04:3E:84:12:00 ...
Service Name: STN-SPP
Service RecHandle: 0x10000
Service Class ID List:
  "Serial Port" (0x1101)
Protocol Descriptor List:
  "L2CAP" (0x0100)
  "RFCOMM" (0x0003)
    Channel: 1

Service Name: AMP-iAP
Service RecHandle: 0x10001
Service Class ID List:
  UUID 128: 00000000-deca-fade-deca-deafdecacaff
Protocol Descriptor List:
  "L2CAP" (0x0100)
  "RFCOMM" (0x0003)
    Channel: 2
  "" (0x1200)

komichi@komichi-MacBookPro:~$ rfccomm bind 1 00:04:3E:84:12:00
Command 'rfccomm' not found, did you mean:
  command 'rfcomm' from deb bluez (5.70-0ubuntu3)
Try: sudo apt install <deb name>
komichi@komichi-MacBookPro:~$ rfccom bind 1 00:04:3E:84:12:00
rfccom: command not found
komichi@komichi-MacBookPro:~$ rfcomm bind 1 00:04:3E:84:12:00
Can't create device: Operation not permitted
komichi@komichi-MacBookPro:~$ sudo rfcomm bind 1 00:04:3E:84:12:00
komichi@komichi-MacBookPro:~$ ls /dev/r
random   rfcomm1  rfkill   rtc      rtc0     
komichi@komichi-MacBookPro:~$ ls /dev/rfcomm1 
/dev/rfcomm1
komichi@komichi-MacBookPro:~$ cd Documents/
komichi@komichi-MacBookPro:~/Documents$ ls
OBD_LINK_Test
komichi@komichi-MacBookPro:~/Documents$ cd OBD
bash: cd: OBD: No such file or directory
komichi@komichi-MacBookPro:~/Documents$ cd OBD_LINK_Test/
komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls
LICENSE  python-obd.py  README.md  test.py
komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls -a
.  ..  .git  .gitignore  LICENSE  python-obd.py  README.md  test.py
komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ python -V
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ python3 -V
Python 3.12.3
komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ python3 -m venv .venv
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.12-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: /home/komichi/Documents/OBD_LINK_Test/.venv/bin/python3

komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ sudo apt install python3.12-venv
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 2 not upgraded.
Need to get 2,423 kB of archives.
After this operation, 2,770 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y 
Get:1 http://jp.archive.ubuntu.com/ubuntu noble/universe amd64 python3-pip-whl all 24.0+dfsg-1ubuntu1 [1,702 kB]
Get:2 http://jp.archive.ubuntu.com/ubuntu noble/universe amd64 python3-setuptools-whl all 68.1.2-2ubuntu1 [715 kB]
Get:3 http://jp.archive.ubuntu.com/ubuntu noble-updates/universe amd64 python3.12-venv amd64 3.12.3-1ubuntu0.1 [5,678 B]
Fetched 2,423 kB in 3s (758 kB/s)           
Selecting previously unselected package python3-pip-whl.
(Reading database ... 173164 files and directories currently installed.)
Preparing to unpack .../python3-pip-whl_24.0+dfsg-1ubuntu1_all.deb ...
Unpacking python3-pip-whl (24.0+dfsg-1ubuntu1) ...
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack .../python3-setuptools-whl_68.1.2-2ubuntu1_all.deb ...
Unpacking python3-setuptools-whl (68.1.2-2ubuntu1) ...
Selecting previously unselected package python3.12-venv.
Preparing to unpack .../python3.12-venv_3.12.3-1ubuntu0.1_amd64.deb ...
Unpacking python3.12-venv (3.12.3-1ubuntu0.1) ...
Setting up python3-setuptools-whl (68.1.2-2ubuntu1) ...
Setting up python3-pip-whl (24.0+dfsg-1ubuntu1) ...
Setting up python3.12-venv (3.12.3-1ubuntu0.1) ...
komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ python3 -m venv .venv
komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ source .venv/bin/activate
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ pip install obd
Collecting obd
  Downloading obd-0.7.2.tar.gz (60 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.6/60.6 kB 1.0 MB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting pyserial==3.* (from obd)
  Downloading pyserial-3.5-py2.py3-none-any.whl.metadata (1.6 kB)
Collecting pint==0.20.* (from obd)
  Downloading Pint-0.20.1-py3-none-any.whl.metadata (7.5 kB)
Downloading Pint-0.20.1-py3-none-any.whl (269 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 269.5/269.5 kB 2.3 MB/s eta 0:00:00
Downloading pyserial-3.5-py2.py3-none-any.whl (90 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.6/90.6 kB 3.3 MB/s eta 0:00:00
Building wheels for collected packages: obd
  Building wheel for obd (pyproject.toml) ... done
  Created wheel for obd: filename=obd-0.7.2-py3-none-any.whl size=72223 sha256=9973eed32ebb0589fd39e350276a942a1ea92ba420737e98ad0451a65657bd25
  Stored in directory: /home/komichi/.cache/pip/wheels/79/ea/cf/8457b04b04a1599e3030326ca99f9c2daf2561619030c9eb18
Successfully built obd
Installing collected packages: pyserial, pint, obd
Successfully installed obd-0.7.2 pint-0.20.1 pyserial-3.5
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls
LICENSE  python-obd.py  README.md  test.py
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ python python-obd.py 
Available ports:  []
No ports found
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls /dev/tty
tty        tty20      tty33      tty46      tty59      ttyS12     ttyS25
tty0       tty21      tty34      tty47      tty6       ttyS13     ttyS26
tty1       tty22      tty35      tty48      tty60      ttyS14     ttyS27
tty10      tty23      tty36      tty49      tty61      ttyS15     ttyS28
tty11      tty24      tty37      tty5       tty62      ttyS16     ttyS29
tty12      tty25      tty38      tty50      tty63      ttyS17     ttyS3
tty13      tty26      tty39      tty51      tty7       ttyS18     ttyS30
tty14      tty27      tty4       tty52      tty8       ttyS19     ttyS31
tty15      tty28      tty40      tty53      tty9       ttyS2      ttyS5
tty16      tty29      tty41      tty54      ttyprintk  ttyS20     ttyS6
tty17      tty3       tty42      tty55      ttyS0      ttyS21     ttyS7
tty18      tty30      tty43      tty56      ttyS1      ttyS22     ttyS8
tty19      tty31      tty44      tty57      ttyS10     ttyS23     ttyS9
tty2       tty32      tty45      tty58      ttyS11     ttyS24     
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls /dev/rf
rfcomm1  rfkill   
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls
LICENSE  python-obd.py  README.md  test.py
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ vim python-obd.py 
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls /dev/
autofs           kmsg          rfcomm1   tty28  tty61      ttyS9
block            kvm           rfkill    tty29  tty62      udmabuf
bsg              log           rtc       tty3   tty63      uhid
btrfs-control    loop0         rtc0      tty30  tty7       uinput
bus              loop1         sda       tty31  tty8       urandom
char             loop10        sda1      tty32  tty9       userfaultfd
console          loop11        sda2      tty33  ttyprintk  userio
core             loop2         sda3      tty34  ttyS0      vcs
cpu              loop3         sg0       tty35  ttyS1      vcs1
cpu_dma_latency  loop4         shm       tty36  ttyS10     vcs2
cuse             loop5         snapshot  tty37  ttyS11     vcs3
disk             loop6         snd       tty38  ttyS12     vcs4
dma_heap         loop7         stderr    tty39  ttyS13     vcs5
dri              loop8         stdin     tty4   ttyS14     vcs6
drm_dp_aux0      loop9         stdout    tty40  ttyS15     vcsa
drm_dp_aux1      loop-control  tty       tty41  ttyS16     vcsa1
drm_dp_aux2      mapper        tty0      tty42  ttyS17     vcsa2
ecryptfs         mcelog        tty1      tty43  ttyS18     vcsa3
fb0              mei0          tty10     tty44  ttyS19     vcsa4
fd               mem           tty11     tty45  ttyS2      vcsa5
full             mqueue        tty12     tty46  ttyS20     vcsa6
fuse             net           tty13     tty47  ttyS21     vcsu
hpet             ng0n1         tty14     tty48  ttyS22     vcsu1
hugepages        null          tty15     tty49  ttyS23     vcsu2
hwrng            nvme0         tty16     tty5   ttyS24     vcsu3
i2c-0            nvme0n1       tty17     tty50  ttyS25     vcsu4
i2c-1            nvme0n1p1     tty18     tty51  ttyS26     vcsu5
i2c-2            nvme0n1p2     tty19     tty52  ttyS27     vcsu6
i2c-3            nvme0n1p3     tty2      tty53  ttyS28     vfio
i2c-4            nvme0n1p4     tty20     tty54  ttyS29     vga_arbiter
i2c-5            nvram         tty21     tty55  ttyS3      vhci
i2c-6            port          tty22     tty56  ttyS30     vhost-net
i2c-7            ppp           tty23     tty57  ttyS31     vhost-vsock
i2c-8            psaux         tty24     tty58  ttyS5      zero
iio:device0      ptmx          tty25     tty59  ttyS6      zfs
initctl          pts           tty26     tty6   ttyS7
input            random        tty27     tty60  ttyS8
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls /dev/rf
rfcomm1  rfkill   
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls /dev/rfcomm1 
/dev/rfcomm1
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ vim python-obd.py 
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ vim python-obd.py 
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ python python-obd.py 
Available ports:  []
No ports found
[obd.obd] ======================= python-OBD (v0.7.2) =======================
[obd.obd] Explicit port defined
[obd.elm327] Initializing ELM327: PORT=/dev/rfcomm1 BAUD=38400 PROTOCOL=6
[obd.elm327] [Errno 13] could not open port /dev/rfcomm1: [Errno 13] Permission denied: '/dev/rfcomm1'
[obd.obd] Closing connection
[obd.obd] Cannot load commands: No connection to car
[obd.obd] ===================================================================
[obd.obd] Query failed, no connection available
None
[obd.obd] Query failed, no connection available
None
[obd.obd] Query failed, no connection available
None
[obd.obd] Query failed, no connection available
None
[obd.obd] Query failed, no connection available
None
[obd.obd] Query failed, no connection available
None
^CTraceback (most recent call last):
  File "/home/komichi/Documents/OBD_LINK_Test/python-obd.py", line 19, in <module>
    time.sleep(1)
KeyboardInterrupt

(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls
LICENSE  python-obd.py  README.md  test.py
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ vim python-obd.py 
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls -al /dev/rfcomm1 
crw-rw---- 1 root dialout 216, 1 Sep 10 18:29 /dev/rfcomm1
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ chowner
chowner: command not found
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ chowr
Command 'chowr' not found, did you mean:
  command 'chown' from deb coreutils (9.4-2ubuntu2)
Try: sudo apt install <deb name>
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ echo $USER
komichi
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ sudo chown $USER /dev/rfcomm1 
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ ls -al /dev/rfcomm1 
crw-rw---- 1 komichi dialout 216, 1 Sep 10 18:29 /dev/rfcomm1
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ python python-obd.py 
Available ports:  ['/dev/rfcomm1']
Using port:  /dev/rfcomm1
[obd.obd] ======================= python-OBD (v0.7.2) =======================
[obd.obd] Explicit port defined
[obd.elm327] Initializing ELM327: PORT=/dev/rfcomm1 BAUD=38400 PROTOCOL=6
[obd.elm327] write: b' \r'
Traceback (most recent call last):
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/serial/serialposix.py", line 398, in _reconfigure_port
    orig_attr = termios.tcgetattr(self.fd)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^
termios.error: (5, 'Input/output error')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/komichi/Documents/OBD_LINK_Test/python-obd.py", line 13, in <module>
    connection = obd.OBD(portstr=ports[0], protocol="6", baudrate=38400, fast=False, timeout=40, start_low_power=True)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/obd/obd.py", line 63, in __init__
    self.__connect(portstr, baudrate, protocol,
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/obd/obd.py", line 93, in __connect
    self.interface = ELM327(portstr, baudrate, protocol,
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/obd/elm327.py", line 146, in __init__
    if not self.set_baudrate(baudrate):
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/obd/elm327.py", line 296, in set_baudrate
    self.__port.baudrate = baud
    ^^^^^^^^^^^^^^^^^^^^
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/serial/serialutil.py", line 299, in baudrate
    self._reconfigure_port()
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/serial/serialposix.py", line 401, in _reconfigure_port
    raise SerialException("Could not configure port: {}".format(msg))
serial.serialutil.SerialException: Could not configure port: (5, 'Input/output error')
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ vim python-obd.py 
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ python python-obd.py 
Available ports:  ['/dev/rfcomm1']
Using port:  /dev/rfcomm1
[obd.obd] ======================= python-OBD (v0.7.2) =======================
[obd.obd] Explicit port defined
[obd.elm327] Initializing ELM327: PORT=/dev/rfcomm1 BAUD=auto PROTOCOL=auto
Traceback (most recent call last):
  File "/home/komichi/Documents/OBD_LINK_Test/python-obd.py", line 13, in <module>
    connection = obd.OBD(portstr=ports[0], fast=False, timeout=40)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/obd/obd.py", line 63, in __init__
    self.__connect(portstr, baudrate, protocol,
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/obd/obd.py", line 93, in __connect
    self.interface = ELM327(portstr, baudrate, protocol,
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/obd/elm327.py", line 146, in __init__
    if not self.set_baudrate(baudrate):
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/obd/elm327.py", line 294, in set_baudrate
    return self.auto_baudrate()
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/obd/elm327.py", line 324, in auto_baudrate
    response = self.__port.read(1024)
               ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/komichi/Documents/OBD_LINK_Test/.venv/lib/python3.12/site-packages/serial/serialposix.py", line 595, in read
    raise SerialException(
serial.serialutil.SerialException: device reports readiness to read but returned no data (device disconnected or multiple access on port?)
(.venv) komichi@komichi-MacBookPro:~/Documents/OBD_LINK_Test$ python python-obd.py 
Available ports:  ['/dev/rfcomm1']
Using port:  /dev/rfcomm1
[obd.obd] ======================= python-OBD (v0.7.2) =======================
[obd.obd] Explicit port defined
[obd.elm327] Initializing ELM327: PORT=/dev/rfcomm1 BAUD=auto PROTOCOL=auto
[obd.elm327] Response from baud 38400: b'\x7f\x7f\r?\r\r>'
[obd.elm327] Choosing baud 38400
[obd.elm327] write: b'ATZ\r'
[obd.elm327] wait: 1 seconds
[obd.elm327] read: b'ATZ\r\r\rELM327 v1.4b\r\r>'
[obd.elm327] write: b'ATE0\r'
[obd.elm327] read: b'ATE0\rOK\r\r>'
[obd.elm327] write: b'ATH1\r'
[obd.elm327] read: b'OK\r\r>'
[obd.elm327] write: b'ATL0\r'
[obd.elm327] read: b'OK\r\r>'
[obd.elm327] write: b'AT RV\r'
[obd.elm327] read: b'14.0V\r\r>'
[obd.elm327] write: b'ATSP0\r'
[obd.elm327] wait: 1 seconds
[obd.elm327] read: b'OK\r\r>'
[obd.elm327] write: b'0100\r'
[obd.elm327] wait: 1 seconds
[obd.elm327] read: b'SEARCHING...\r7E8 06 41 00 BF 9F A8 93 \r\r>'
[obd.elm327] write: b'ATDPN\r'
[obd.elm327] read: b'A6\r\r>'
[obd.protocols.protocol] map ECU 0 --> ENGINE
[obd.protocols.protocol] map ECU 1 --> TRANSMISSION
[obd.elm327] Connected Successfully: PORT=/dev/rfcomm1 BAUD=38400 PROTOCOL=6
[obd.obd] querying for supported commands
[obd.obd] Sending command: b'0100': Supported PIDs [01-20]
[obd.elm327] write: b'0100\r'
[obd.elm327] read: b'7E8 06 41 00 BF 9F A8 93 \r\r>'
[obd.obd] Sending command: b'0120': Supported PIDs [21-40]
[obd.elm327] write: b'0120\r'
[obd.elm327] read: b'7E8 06 41 20 B1 05 B1 1F \r\r>'
[obd.obd] Sending command: b'0140': Supported PIDs [41-60]
[obd.elm327] write: b'0140\r'
[obd.elm327] read: b'7E8 06 41 40 7E DC 00 00 \r\r>'
[obd.obd] Sending command: b'0600': Supported MIDs [01-20]
[obd.elm327] write: b'0600\r'
[obd.elm327] read: b'7E8 06 46 00 CC 00 00 01 \r\r>'
[obd.obd] Sending command: b'0620': Supported MIDs [21-40]
[obd.elm327] write: b'0620\r'
[obd.elm327] read: b'7E8 06 46 20 C0 00 00 01 \r\r>'
[obd.obd] Sending command: b'0640': Supported MIDs [41-60]
[obd.elm327] write: b'0640\r'
[obd.elm327] read: b'7E8 06 46 40 00 00 00 01 \r\r>'
[obd.obd] Sending command: b'0660': Supported MIDs [61-80]
[obd.elm327] write: b'0660\r'
[obd.elm327] read: b'7E8 06 46 60 00 00 00 01 \r\r>'
[obd.obd] Sending command: b'0680': Supported MIDs [81-A0]
[obd.elm327] write: b'0680\r'
[obd.elm327] read: b'7E8 06 46 80 00 00 00 01 \r\r>'
[obd.obd] Sending command: b'06A0': Supported MIDs [A1-C0]
[obd.elm327] write: b'06A0\r'
[obd.elm327] read: b'7E8 06 46 A0 FE 00 00 00 \r\r>'
[obd.obd] Sending command: b'0900': Supported PIDs [01-20]
[obd.elm327] write: b'0900\r'
[obd.elm327] read: b'7E8 06 49 00 14 40 00 00 \r\r>'
[obd.OBDCommand] Message was shorter than expected (6<7). Padded message: bytearray(b'I\x00\x14@\x00\x00\x00')
[obd.obd] finished querying with 120 commands supported
[obd.obd] ===================================================================
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
[obd.obd] Sending command: b'010D': Vehicle Speed
[obd.elm327] write: b'010D\r'
[obd.elm327] read: b'7E8 03 41 0D 00 \r\r>'
0.0 kilometer_per_hour
^CTraceback (most recent call last):
  File "/home/komichi/Documents/OBD_LINK_Test/python-obd.py", line 19, in <module>
    time.sleep(1)
KeyboardInterrupt

