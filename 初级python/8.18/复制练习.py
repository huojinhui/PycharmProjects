file = open('笔记(26).txt', 'r', encoding='utf - 8')
new_file = open('笔记1.txt', 'w', encoding='utf - 8')
for i in file:
    new_file.write(i)
print(file.readlines(3))