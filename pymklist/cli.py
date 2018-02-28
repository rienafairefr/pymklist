# -*- coding: utf-8 -*-

"""Console script for pymklist."""
import sys
import click
import os

import re
from six.moves import input as six_input

from pymklist.download_data import dowload_data




ldraw = re.compile(r'ldraw', flags=re.IGNORECASE)
yes = re.compile(r'[y](?:es)?', flags=re.IGNORECASE)


@click.command(name='make-list')
def main(input_directory=None):
    """Console script for pymklist."""
    if input_directory is None:
        current_directory = os.path.basename(os.getcwd())
        if re.match(ldraw, current_directory) and os.path.exists('parts'):
            print('operating from a LDraw folder, continuing...')
            directory = 'parts'
        elif not re.match(ldraw, current_directory):
            print('LDraw parts directory not found')
            print('Please specify the LDraw parts library directory location in the arguments of the make-list call')
            raise click.Abort()
        else:
            print('LDraw parts directory not found')
            input_directory = os.getcwd()
            answer = six_input('Do you want it downloaded to a ldraw directory in %s?' % input_directory)
            if re.match(yes, answer):
                dowload_data(input_directory)
                directory = os.path.join('parts')
            else:
                print('Can\'t continue without a LDraw parts directory')
                raise click.Abort()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
