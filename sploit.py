#!/usr/bin/env python
#-*- encoding: utf-8 -*-
# vi: set ft=python :

from pwn import *
import optparse
import sys
import os
from genrr2 import GenRR2
from Parser import Parser
from Engine import Engine

BOLD_RED="\033[1;31m"
END="\033[0m"

_logo_="""\033[1;31m
  @@@@@@ @@@@@@@  @@@       @@@@@@  @@@ @@@@@@@
 !@@     @@!  @@@ @@!      @@!  @@@ @@!   @@!
  !@@!!  @!@@!@!  @!!      @!@  !@! !!@   @!!
     !:! !!:      !!:      !!:  !!! !!:   !!:
 ::.: :   :       : ::.: :  : :. :  :      :
\033[0m"""

def main():

    print _logo_
    config=Parser().parse()

    if config["mode"] == "debug":
        try:
            #print "\033[1;32m[+] Generating rr2 file\033[0m %s" % (config["rr2path"])
            tmp=GenRR2(config).gen_rr2(stream="A"*40)
            Engine(config).launch_debugger(tmp)

            print ""
        finally:
            os.remove(tmp)
        
if __name__ == '__main__':
    main()