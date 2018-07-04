import sys
import getopt

opts, args = getopt.gnu_getopt(cmdline_params, 'hc:', ['help', 'config='])

for option, parameter in opts:

    if option == '-h' or option == '- -help':
        print("This program can be run with either -h or - -help for this message,")
        print("or with -c or - -config=<file> to specify a different configuration file")

    if option in ('-c', '- -config'): # this means the same as the above
        print("Using configuration file %s" % parameter)
