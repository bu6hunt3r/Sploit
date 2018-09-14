# vi: set ft=python
from Checker import check_breakpoints
import os
class Engine():
    def __init__(self, config):
        self._config=config
    
    def enable_breakpoints(self):
        if self._config["breakpoints"] and check_breakpoints(self._config["breakpoints"]):
            c=0
            bps=[]
            for bp in map(str.strip, self._config["breakpoints"].split(",")):
                c+=1
                bps.append(bp)
                print "[i] Enabling BP_%d: %s" % (c,bp)

        return bps

    def launch_debugger(self, tmp):
        dbg_cmd="r2 -e dbg.profile=%s -d %s " % (tmp, self._config["binpath"])
        bps=self.enable_breakpoints()

        if bps:
            if len(bps) == 1:
                dbg_cmd+="-c 'db %s'" % bps[0]
            else:
                dbg_cmd+="-c '"
                for bp in bps:
                    dbg_cmd+="db %s; " % bp

                dbg_cmd+="'"

        os.system("%s" % dbg_cmd)
        
