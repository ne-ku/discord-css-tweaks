import re

STYLE_FORMAT = r'^discord\.com##(.*):style\((.*)\)$'
REMOVE_FORMAT = r'^discord\.com##(.*)$'

with open('ublock-filters.txt', 'r') as f:
    lines = f.readlines()

result = ''
for line in lines:
    if re.match(STYLE_FORMAT, line):
        line = re.sub(STYLE_FORMAT, r'\1 {\n    \2\n}\n', line[:-1])
        line = re.sub(r';+[\t ]*', ';\n    ', line)
        result += re.sub(r'([^;])\n}', r'\1;\n}', line)
    elif re.match(REMOVE_FORMAT, line):
        result += re.sub(REMOVE_FORMAT, r'\1 {\n    display: none;\n}\n', line[:-1])
    elif line.startswith('!'):
        result += re.sub(r'![\t ]*(.*)', r'/* \1 */', line)
    elif line == '\n':
        result += '\n'
    else:
        result += '/*' + line[:-1] + '*/\n'

with open('stylesheet.css', 'w') as f:
    f.write(result)
