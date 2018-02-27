from googletrans import Translator
from utilities.GeneralUtilities import print_say
from googletrans.constants import LANGCODES, LANGUAGES, SPECIAL_CASES
import six

def main(self):
    branch = set()
    _main(self, branch)
    with open('main@translate.py.branch', 'a') as branch_file:
        branch_file.write('total: %s\n' % str(18))
        branch_file.write('activated: %s\n' % str(len(branch)))
        branch_file.write('set: %s\n' % str(branch))
        branch_file.write('--------------\n')

def _main(self, branch):

    '''
        source language
    '''

    print_say('\nEnter source language ', self)
    if six.PY2:
        branch.add(23)
        srcs = raw_input()
    else:
        branch.add(26)
        srcs = input()
    while (srcs not in LANGUAGES) and (srcs not in SPECIAL_CASES) and (srcs not in LANGCODES):
        branch.add(29)
        if srcs in SPECIAL_CASES:
            branch.add(31)
            srcs = SPECIAL_CASES[srcs]
        elif srcs in LANGCODES:
            branch.add(34)
            srcs = LANGCODES[srcs]
        else:
            branch.add(37)
            print_say("\nInvalid source language\nEnter again", self)
            if six.PY2:
                branch.add(40)
                srcs = raw_input()
            else:
                branch.add(43)
                srcs = input()
    print_say('\nEnter destination language ', self)
    if six.PY2:
        branch.add(47)
        des = raw_input()
    else:
        branch.add(50)
        des = input()
    while (des not in LANGUAGES) and (des not in SPECIAL_CASES) and (des not in LANGCODES):
        branch.add(53)
        if des in SPECIAL_CASES:
            branch.add(55)
            des = SPECIAL_CASES[des]
        elif des in LANGCODES:
            branch.add(58)
            des = LANGCODES[des]
        else:
            branch.add(61)
            print_say("\nInvalid destination language\nEnter again", self)
            if six.PY2:
                branch.add(64)
                des = raw_input()
            else:
                branch.add(67)
                des = input()
    print_say('\nEnter text ', self)
    if six.PY2:
        branch.add(71)
        tex = raw_input()
    else:
        branch.add(74)
        tex = input()
    translator = Translator()
    result = translator.translate(tex, dest=des, src=srcs)
    result = u"""
[{src}] {original}
    ->
[{dest}] {text}
[pron.] {pronunciation}
    """.strip().format(src=result.src, dest=result.dest, original=result.origin,
                       text=result.text, pronunciation=result.pronunciation)
    print(result)
