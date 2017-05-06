"""
Amity space allocation, the example uses docopt to demonstrate
an interactive command line application

Usage:
    amity create_room<room_name><room_type>
    amity add_person<first_name><last_name><job_type>[<want_accomodation>]
    amity reallocate_person
    amity load_people
    amity print_allocations
    amity print_unallocated
    amity print_rooms
    amity save_state
    amity load_state
    amity -h | --help
    amity ---version

Options:
    h, --help   Shows the screen
    --version   Prints the version

"""
from docopt import docopt, DocoptExit

def docopt_cmd(func):  
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as exit:
            # The is thrown when the args do not match.

            print('Invalid Command!')
            print(exit)
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
