# sysref
Terminal Linux Syscall Reference Table for x86 and x64

# Dependencies
pip3 -r requirements.txt

# Usage
./sysref.py -a (architecture) (keyword)
<br />
<br />
Examples:
<br />
<br />
  python3 sysref.py -a x86 -s sys_open
  <br />
  python3 sysref.py -a x86 dup
<br />

# TODO


<br />
-Providing HTML output
-Support for ARM architectures


# Thanks

This sript was heavily inspired by:

  -https://syscalls.kernelgrok.com
  <br />
   <br />
  -Filippo Valsorda's https://filippo.io/linux-syscall-table/
  
  <br />
  
For a long time, I checked the pages above for writing assembly. They are both great projects that will make your life easier. I find it easier having them both in one place, accessible via terminal. 


