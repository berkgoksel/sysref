# sysref
Linux Syscall Reference Table for x86, x64, arm32 and arm64, searchable via CLI.


## Usage
```
$ pip3 install -r requirements.txt
$ python3 sysref.py -a <architecture> <keyword>
```

### Example Usage
```
$ python3 sysref.py -a x86 -s sys_open
$ python3 sysref.py -a x86 dup
```

## TODO
- Add argument for shorter output (no reference, no syscall number)
- Provide HTML output
- Support for RISC-V

## Acknowledgements
Syscall table for x86:
- [Linux Syscall Reference](https://syscalls.kernelgrok.com)

Syscall table for x64:
- Filippo Valsorda's [Searchable Linux Syscall Table for x86 and x86_64](https://filippo.io/linux-syscall-table/)

- Syscall tables for arm32 and arm64:
https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md
