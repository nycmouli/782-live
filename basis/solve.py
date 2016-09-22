#!/Users/nycmouli/anaconda/bin/python
from basis import msg
def examples():
    """Prints examples of using the script to the console using colored output.                                                   
    """
    script = "Basis: 1D Quantum potential Solver via Basis Expansion."
    explain = ("For simple 1D potentials such as Kronig penny. The code produces"
               "numerical solutions.")
    contents = [(("Solve the potetial in `kp.cfg` using 200 basis funtions"),
                 "solve.py 200 -potential kp.cfg",
                 "This solves the solution to the default `output.dat' "),
                (("Solve the potetial `sho.cfg`, save the solution to "
                  " `mysol.out`."),
                 "solve.py 400 -potential sho.cfg -outfile mysol.out","")]
    required = ("REQUIRED: potential config file `pot.cfg`")
    output = ("RETURNS: plot window; for logging-only mode, the data being "
              "logged is also periodically printed to stdout.")
    details = ("The plotting uses `matplotlib` with the default configured "
               "backend. If you want a different backend, set the rc config "
               "for `matplotlib` using online documentation. However, many "
               "backends don't play well with the animation (depending on OS "
               "type and version, etc., etc.; so use carefully.")
    outputfmt = ("")

    msg.example(script, explain, contents, required, output, outputfmt, details)


script_options = {
    "N": dict(default="100",type=int,
              help=("Specifies how many basis functions to use in the expansion solution.")),
    "-plot": dict(action="store_true",
                  help=("Plots the solution")),
    "-autoconf": {"action": "store_true",
                  "help": ("Runs in automatic mode by loading a "
                           "configuration file in the current directory "
                           "called 'sensors.cfg'.")},
    "-config": {"help": ("Specify a configuration file to get sensor "
                         "setup information from.")},
    }
"""dict: default command-line arguments and their                                                                                              
    :meth:`argparse.ArgumentParser.add_argument` keyword arguments.                                                                            
"""


def _parser_options():
    """Parses the options and arguments from the command line."""
    #We have two options: get some of the details from the config file,                                                                        
    import argparse
    from basis import base
    pdescr = "1D-qunatum solver"
    parser = argparse.ArgumentParser(parents=[base.bparser], description=pdescr)
    for arg, options in script_options.items():
        parser.add_argument(arg, **options)

    args = base.exhandler(examples, parser)
    if args is None:
        return
    return args

def run(args):
    print("Running",args)
    return 0

if __name__ == '__main__': # pragma: no cover                                                                                     
    run(_parser_options())
