# sysref
Linux Syscall Reference Table for x86 and x64, searchable via CLI


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
- Providing HTML output
- Support for ARM architectures

## Acknowledgments
For a long time, I checked the pages below for writing assembly. They are both great projects that will make your life
easier. I find it easier having them both in one place, accessible via terminal.
- [Linux Syscall Reference](https://syscalls.kernelgrok.com)
- Filippo Valsorda's [Searchable Linux Syscall Table for x86 and x86_64](https://filippo.io/linux-syscall-table/)
