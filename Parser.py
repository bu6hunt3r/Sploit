import argparse
import sys

class Parser():
    """Parses tool's arguments
    """
    def __init__(self):
        self.config={}

    def parse(self):
        """Parse sploit arguments
        """

        parser=argparse.ArgumentParser(description="""\
            \033[4;32mSploit debugging / development frontend\033[0m
        """)
        subparsers=parser.add_subparsers(help="Sploit mode (d debug | a another)", dest="mode")
        debug_parser=subparsers.add_parser("d")
        another_parser=subparsers.add_parser("a")
        debug_parser.add_argument("-p","--binpath", type=str, help="Path to binary", required=True)
        debug_parser.add_argument("-b","--breakpoints", type=str, help="Breakpoints to enable", required=True)
        #debug_parser.add_argument("-r","--rr2path", type=str, help="Path to rarun2 file", required=True)
        debug_parser.add_argument("-i","--payload",type=str, help="Path to payload", required=True)
        debug_parser.add_argument("-x","--execute",type=str, help="Additional r2 cmd", required=False)

        if len(sys.argv) == 1:
            parser.print_help(sys.stderr)

        args=parser.parse_args()

        self._load_config(args)

        return self.config

    def _load_config(self, args):
        """Load configuration from parsed arguments
        """
        if args.mode == "d":
            self.config = {
                "binpath": args.binpath,
                "breakpoints": args.breakpoints,
                #"rr2path": args.rr2path,
                "payload": args.payload,
                "cmd": args.execute,
                "mode": "debug"
            }
