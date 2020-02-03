# sysref
Terminal Linux Syscall Reference Table for x86 and x64

# Usage

./sysref.py -a <architecture> <keyword>

Examples:
  python3 sysref.py -a x86 -s sys_open
  python3 sysref.py -a x86 dup


# TODO

-Parsing x86_64 Reference table.
-Providing HTML and greppable plaintext output 


# Thanks

This sript was heavily inspired by:

  -https://syscalls.kernelgrok.com
  -Filippo Valsorda's https://filippo.io/linux-syscall-table/
  
  
For a long time, I checked the pages above for writing assembly. They are both great projects that will make your life easier. I find it easier having them both in one place, accessible via terminal. 


