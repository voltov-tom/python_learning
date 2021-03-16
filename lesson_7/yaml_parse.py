import os

with open('config.yaml', 'r', encoding='utf-8') as yaml:
    for line in yaml:
        line = line.strip().replace('\n', '')
        if not os.path.exists(line):
            file = os.path.basename(line)
            if '.' in file:
                file = open(line, 'w')
            else:
                os.makedirs(line)
