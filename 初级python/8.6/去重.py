score = [11, 12, 13, 14, 15, 11, 12, 45, 13]
new = []
for i in score:
    if i not in new:
        new.append(i)
print(new)