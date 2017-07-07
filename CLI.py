
"""
This ProTrack uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    track_program add_skill <arg>
    track_program learnt_skill <arg>
    track_program list_skills
    track_program done_skills
    track_program undone_skills
    track_program show_progress
    track_program (-i | --interactive)
    track_program (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from protrack import Protrack


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


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my ProTrack program!' \
        + ' (type help for a list of commands.)'
    prompt = '(ProTrack) '
    protrack = Protrack()
    file = None

    def __init__(self):
        self.protrack = Protrack()

    @docopt_cmd
    def do_add_skill(self, arg):
        """Usage: add_skill <arg> """
        self.protrack.add_skill(arg)

        print(arg)

    @docopt_cmd
    def do_learn_skill(self, arg):
        """Usage: learnt_skill <arg> """
        self.protrack.learn_skill(arg)


        print(arg)

    def do_quit(self, arg):
        """Quits out of ProTrack Mode."""

        print('Good Bye!')


        exit()

    def do_list_all_skills(self):
        """Usage: list_skills  """
        self.protrack.list_all_skills()


    def do_list_done_skills(self):
        """Usage: done_skill  """
        self.protrack.list_done_skills()

    def do_list_undone_skills(self):
        """Usage: undone_skill """
        self.protrack.list_undone_skills()


    def do_show_progress(self):
        """Usage: show_progress """
        self.protrack.show_progress()



opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
