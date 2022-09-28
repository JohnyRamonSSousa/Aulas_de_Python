
with open('arquivo.txt') as f:
    content = f.readlines()


content = [x.strip('\n') for x in content]

print(content)

for line in content:
    print(line)