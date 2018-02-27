import re
from os import listdir
from os.path import isfile, join

""" quick and dirty script for sumarizing coverage data """

branchdata = dict()

path='.'
branchfiles = [f for f in listdir(path) if isfile(join(path, f)) and f[-6:]=='branch']
for b in branchfiles:

    content = None
    with open(b, 'r') as f:
        content = f.read()

    if not content or len(content)==0:
        # assume no coverage if branch-file empty
        branchdata[b] = 0
        continue

    block_total = list();
    block_members = set()

    pattern_block = r'(.*\n.*\n.*\n-+)'
    match_blocks = re.findall(pattern_block, content)
    for block in match_blocks:

        pattern_total = r'(?:total: )(\d+)'
        block_total.append(re.findall(pattern_total, block)[0])

        pattern_set = r'(?:set\(\[).*'
        setmatch = re.findall(pattern_set, block)

        pattern_member = r'\d+'
        block_members = block_members | set(re.findall(pattern_member, setmatch[0]))

    branchdata[b] = {
        'total': block_total[0],
        'activations': len(block_members),
        'coverage': float(len(block_members)) / max(1, float(int(block_total[0]))),
        'times_invoked': len(block_total),
        'activated_lines': block_members,
    }

print '%-20s %-15s %-15s %-15s %-s' % (
    'Function',
    'Times invoked',
    'Branches',
    'Activations',
    'Coverage'
)
print '-'*77
for key in branchdata:
    branch = branchdata[key]
    print '%-20s %-15s %-15s %-15s %-s%%' % (
        key[:-7],
        0 if key not in branchdata else branchdata[key]['times_invoked'],
        0 if key not in branchdata else branchdata[key]['total'],
        0 if key not in branchdata else branchdata[key]['activations'],
        0 if key not in branchdata else str(int(round(branchdata[key]['coverage'], 2)*100))
    )
