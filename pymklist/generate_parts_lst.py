import glob
import os
import shutil

import re
import string

from pymklist.utils import preserve_cwd


@preserve_cwd
def generate_parts_lst(input_directory, mode):
    os.chdir(input_directory)
    if os.path.exists('parts.lst'):
        shutil.move('parts.lst', 'parts.lst.old')

    parts = glob.glob(os.path.join('parts', '*.dat'))

    parts_dict = {'_':[], '~':[]}
    parts_lst = []

    format_string = '{filename:<30} {description}'

    def line_format(**kwargs):
        return format_string.format(**kwargs)

    for part in parts:
        filename = os.path.basename(part)
        number, _ = os.path.splitext(filename)
        with open(part, 'r') as part_file:
            header = part_file.readline()
            header_description = header[2:]
            if '~Moved' in header:
                continue
            row = {'filename': filename, 'number': number, 'description': header_description}

            if '_' in header_description:
                parts_dict['_'].append(row)
            elif '~' in header_description:
                parts_dict['~'].append(row)
            else:
                parts_lst.append(row)

    alphanum = re.compile('[\W_]+', re.UNICODE)

    def cmpkey1(row):
        return alphanum.sub('', row[mode]).lower()

    def cmpkey2(row):
        return line_format(**row)

    def do_sort(li):
        li.sort(key=cmpkey2)
        li.sort(key=cmpkey1)


    part1 = parts_lst[2573]
    part2 = parts_lst[674]

    do_sort(parts_lst)
    do_sort(parts_dict['_'])
    do_sort(parts_dict['~'])

    parts_lst.extend(parts_dict['_'])
    parts_lst.extend(parts_dict['~'])

    open('parts.lst', 'w').writelines(line_format(**row) for row in parts_lst)
