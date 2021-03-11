from collections import Counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    with open('new_file.txt', 'w', encoding='utf-8') as new_f:
        for line in f:
            line = line.replace('"', '')
            line = line.split(' ')
            new_line = line[0], '\n'
            new_f.writelines(new_line)

with open('new_file.txt', 'r', encoding='utf-8') as new_f:
    spamer = Counter(new_f).most_common()
with open('new_file.txt', 'w', encoding='utf-8') as new_f:
    for line in spamer:
        line = str(line)
        new_f.write(line + '\n')

# думаю, что-бы не загружать ОЗУ ПК, нужно использовать запись в файлы,
# чтобы данные хранились в них, а не в переменных(ОЗУ)
