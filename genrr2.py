# vi: set ft=python :
from Checker import check_path
import tempfile

class GenRR2():
    def __init__(self, config):
        self._config=config

    def gen_payload(self, stream):
        try:
            with open(self._config["payload"],"wb") as f:
                f.write(stream)
        except Exception as e:
            print e
    
    def gen_rr2(self, stream):
        for p in "binpath payload".split():
            if not check_path(self._config[p]):
                raise Exception("Invalid path \033[1;31m%s\033[0m" % p)

        self.gen_payload(stream)

        try: 
            tmprr2=tempfile.mktemp()
            with open(tmprr2, "w") as f:
                print "\033[1;32m[+] Generating rr2 file\033[0m %s" % (tmprr2)
                f.write("'!/usr/bin/rarun2\nprogram=%s\nstdin=%s\n" % (self._config["binpath"], self._config["payload"]))
        except Exception as e:
            print e
        
        return tmprr2