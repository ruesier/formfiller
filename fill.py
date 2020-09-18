#! /usr/bin/python3
import re

fillable = re.compile(r'__(\w+)__')

def extractFormKeys(form):
    seen = set()
    for match in fillable.finditer(form):
        key = match.group(1)
        if key not in seen:
            seen.add(key)
            yield key

def populateForm(form, data):
    def replace(match):
        return data[match.group(1)]
    return fillable.sub(replace, form)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('expecting form as a text file for first arguement\nfile.py path/to/form.txt')
    with open(sys.argv[1]) as formfile:
        form = formfile.read()
    data = {k: input(f'{k}: ') for k in extractFormKeys(form)}
    print(populateForm(form, data))
