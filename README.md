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
For a long time, I checked the pages below for writing assembly. They are both great projects that will make your life
easier. I find it easier having them both in one place, accessible via terminal.
- [Linux Syscall Reference](https://syscalls.kernelgrok.com)
- Filippo Valsorda's [Searchable Linux Syscall Table for x86 and x86_64](https://filippo.io/linux-syscall-table/)

- For arm32 and arm64, syscall tables I have used can be found at: https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md
