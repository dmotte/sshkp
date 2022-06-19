#!/usr/bin/env python3

import argparse
import getpass
import os
import sys

from pykeepass import PyKeePass


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(description='''
        Executes an SSH command with a password from a KeePass database.
        This script supports two environment variables: KP_FILENAME (mandatory)
        and KP_PASSWORD (optional)
    ''')

    parser.add_argument('entryname', metavar='ENTRYNAME', type=str,
                        help='KeePass entry name')
    parser.add_argument('command', metavar='COMMAND', nargs=argparse.REMAINDER,
                        help='''SSH command. If the command equals to ".print",
                        then it just prints the password without executing
                        anything else''')

    args = vars(parser.parse_args(argv[1:]))

    ############################################################################

    entryname = args['entryname']
    command = args['command']

    kp_filename = os.getenv('KP_FILENAME')
    kp_password = os.getenv('KP_PASSWORD')

    if kp_filename is None:
        raise Exception('KP_FILENAME environment variable not defined')
    if kp_password is None:
        kp_password = getpass.getpass('KeePass password: ')

    ############################################################################

    kp = PyKeePass(kp_filename, kp_password)

    entry = kp.find_entries_by_title(entryname, first=True)

    if entry is None:
        raise Exception('KeePass entry not found')

    ############################################################################

    if len(command) >= 1 and command[0] == '.print':
        print(entry.password)
        return 0

    os.environ['SSHPASS'] = entry.password

    os.execv(
        '/usr/bin/sshpass',
        ['sshpass', '-e', 'ssh', entryname] + command,
    )
