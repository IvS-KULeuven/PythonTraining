import argparse
import logging

parser = argparse.ArgumentParser(description="An example for parsing commandline arguments")

parser.add_argument('-X', '--eXtended', action='store_true', help="use the extended version")
parser.add_argument('--log', action='store', 
                    metavar='logfile',
                    help="send logging messages to the specified file")
parser.add_argument('--level', 
                    choices=('DEBUG', 'INFO', 'WARNING', 'ERROR'),
                    help='set the logging level')
parser.add_argument('--max', type=int, help='give the maximum number of ....')
parser.add_argument(dest='filenames', metavar="filename", nargs='*')

args = parser.parse_args()

print (f"args = {args}")
print (f"args.eXtended = {args.eXtended}")
print (f"args.log = {args.log}")
print (f"args.level = {args.level}")
print (f"args.max = {args.max} (type={type(args.max)})")
print (f"args.filenames = {args.filenames}")

log_level = args.level or 'INFO'

if args.log:
    logging.basicConfig(filename=args.log, filemode='w', level=log_level)
else:
    logging.basicConfig(level=log_level)

logging.debug('This is a debug logging message')
logging.info('This is a info logging message')
logging.warning('This is a warning logging message')
logging.error('This is a error logging message')
logging.info(f"The maximum number of ... is {args.max})")
