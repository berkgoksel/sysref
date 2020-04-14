#!/usr/bin/env python3

import re
import sys
import argparse
from tabulate import tabulate


#headers_x86 =  ["num", "syscall", "eax", "ebx", "ecx", "edx", "esi", "edi", "REF"]
#headers_x86_64 = ["num", "syscall", "rax", "rdi", "rsi", "rdx", "r10", "r8", "r9", "REF"]
#headers_arm32 = ["num", "syscall", "r7", "r0", "r1", "r2", "r3", "r4", "r5"]
#headers_arm64 = ["num", "syscall", "x8", "x0", "x1", "x2", "x3", "x4", "x5", "REF"]


def get_table(file):

        table = []
        for line in file:
                line = line.strip("\n")
                line = line.split(",")
                table.append(line)
        return table


def open_file(arch):

        #parse arch
        if arch == "x86":
                headers = ["num", "syscall", "eax", "ebx", "ecx", "edx", "esi", "edi", "REF"]
                file = open("intel_x86.csv", "r")

        elif arch == "x64":
                headers = ["num", "syscall", "rax","rdi", "rsi", "rdx", "r10", "r8", "r9", "REF"]
                file = open("intel_x86_64.csv", "r")

        elif arch == "arm32":
                headers = ["num", "syscall", "r7", "r0", "r1", "r2", "r3", "r4", "r5"]
                file = open("arm32.csv", "r")

        elif arch == "arm64":
                headers = ["num", "syscall", "x8", "x0", "x1", "x2", "x3", "x4", "x5", "REF"]
                file = open("arm64.csv", "r")

        else:
                print("You have specified an architecture that is not supported")
                sys.exit(0)

        table = get_table(file)

        return [file, table, headers]


def wide_search(keyword, file_tuple, tformat):
        print("")

        newtable = []
        for array in file_tuple[1]:
                for element in array:
                        if re.search(keyword, element):
                                newtable.append(array)
                                break

        if (tformat == 'table'):
                print(tabulate(newtable, file_tuple[2], tablefmt="fancy_grid"))


        elif (tformat == 'text'):
                for a in range(len(newtable)):
                        print(' '.join(newtable[a]))


        file_tuple[0].close()


def strict_search(keyword, file_tuple, tformat):

        print("")

        newtable = []
        for array in file_tuple[1]:
                for element in array:
                        if (element == keyword):
                                newtable.append(array)
                                break

        if (tformat == 'table'):
                print(tabulate(newtable, file_tuple[2], tablefmt="fancy_grid", showindex=False))


        elif (tformat == 'text'):
                for a in range(len(newtable)):
                        print(','.join(newtable[a]))
        else:
                sys.exit("You have provided an invalid format.")



        file_tuple[0].close()


def main():

        parser = argparse.ArgumentParser()
        parser.add_argument("keyword", help="Keyword to search for")
        parser.add_argument("-a", "--arch", type=str, required=True,
                help="Architecture to search for syscalls(x86, x64, arm32, arm64)")
        parser.add_argument("-s", "--strictsearch", action="store_true",
                help="Perform a specific syscall search(format: sys_open).")
        parser.add_argument('--format', nargs='?', default='table', type=str, 
                help="The format to print the table out (table/text)")

        try:
                args=parser.parse_args()
        except:
                print("\n")
                sys.exit(0)

        file_tuple = open_file(args.arch)

        if args.strictsearch:
                strict_search(args.keyword, file_tuple, args.format)
        else:
                wide_search(args.keyword, file_tuple, args.format)


        sys.exit(0)



if __name__== "__main__":
        main()
