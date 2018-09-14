# vi: set ft=python :
import os, sys
import re

def check_path(p):
    path=os.path.dirname(p)
    if path and os.access(path, os.W_OK):
        return True

def check_breakpoints(bps):
    bp_regex="(^0x[0-9a-fA-F]{,16},?\s?)(0x[0-9a-fA-F]{,16},?\s?)?$"
    bp_regex=re.compile(bp_regex)

    if not bp_regex.match(bps):
        print "Breakpoints must match i.e: 0xffffffe4, 0x804a040"
        sys.exit(-1)
    else:
        return True



