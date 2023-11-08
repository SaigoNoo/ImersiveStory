from code import Extensions
from argparse import ArgumentParser
from code import read_ini

args = ArgumentParser(description=f"{read_ini('TITLE')} - {read_ini('VERSION')}")
cli = args.add_argument_group('CLI')
cli.add_argument('-c', '--cli', help="Run in CLI mode", action='store_true')
gui = args.add_argument_group('GUI')
gui.add_argument('-g', '--gui', help="Run in GUI mode (not available)", action='store_true')
arg = args.parse_args()

Extensions().extensions()
