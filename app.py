#!/usr/bin/env python
"""
Usage:
    amity add_person <first_name> <last_name> <job_type> [<want_accomodation>]
    amity create_room <room_name> <room_type>
    amity print_allocations [--o=<file_name>]
    amity reallocate_person <first_name> <last_name> <room_name>
    amity print_room <room_name>
    amity print_unallocated [--o=<file_name>]
    amity load_people <filename>
    amity save_state [--db=<db_name]
    amity load_state [--db=<db_name]
    amity (-i | --interactive)
    amity (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import os
import cmd
from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint
from models.amity import Amity

amity = Amity()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    cprint(figlet_format('Amity!', font='calgphy2'),
           'green',)
    print('Welcome to Amity! Here is a list of commands to get you started.' +
          " Type 'help' anytime to access documented commands")
    cprint(__doc__, 'green')


class Interactive(cmd.Cmd):
    prompt = '(Amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_name> <room_type>"""

        room_name = args['<room_name>']
        room_type = args['<room_type>']
        cprint(amity.create_room(room_name, room_type), 'green')

    @docopt_cmd
    def do_add_person(self, args):
        """
        Usage: add_person <first_name> <last_name> <job_type> [<want_accomodation>]
         """
        first_name = args['<first_name>']
        last_name = args['<last_name>']
        job_type = args['<job_type>']
        want_accomodation = args['<want_accomodation>']
        print(amity.add_person(first_name, last_name, job_type, want_accomodation))

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <first_name> <last_name> <room_name>"""

        first_name = args['<first_name>']
        last_name = args['<last_name>']
        room_name = args['<room_name>']

        print(amity.reallocate_person(first_name, last_name, room_name))

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_people <file_name>"""

        file_name = args['<file_name>']
        print (amity.load_people(file_name))

    @docopt_cmd
    def do_print_allocations(self, args):
        """
        Usage: print_allocations [--o=file_name]

        """

        file_name = args['--o']
        amity.print_allocations(file_name)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [--o=<file_name>]

         """
        file_name = args['--o']
        amity.print_unallocated(file_name)

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""

        room_name = args['<room_name>']
        amity.print_room(room_name)

    @docopt_cmd
    def do_save_state(self, args):
        """
        Usage: save_state [--db=<db_name]

        """

        db_name = args['--db']
        amity.save_state(db_name)

    @docopt_cmd
    def do_load_state(self, args):
        """
        Usage: load_state <db_name>

        """
        db_name = args['<db_name>']
        amity.load_state(db_name)

    def do_clear(self, arg):
        """Clears screen"""

        os.system("clear")

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print("Don't be a stranger. Welcome back again!")
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    os.system("clear")
    intro()
    Interactive().cmdloop()

print(opt)
