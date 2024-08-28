relations = dict()
tellers = set()
pending = []

n = int(input())

for _ in range(n):
    line = input().split()
    if line[1] == "??":
        pending.append((line[0], line[2]))
    else: 
        relations[line[2]] = line[0]
        tellers.add(line[0])

updated = True
while updated and pending:
    updated = False
    i = 0
    while i < len(pending):
        pair = pending[i]
        if pair[0] in relations:
            relations[pair[1]] = pair[0]
            updated = True
            pending.pop(i)
        elif pair[1] in relations:
            relations[pair[0]] = pair[1]
            updated = True
            pending.pop(i)
        else:
            i += 1
        
sospects = set()
for pair in pending:
    sospects.add(pair[0])
    sospects.add(pair[1])

sospects.update(tellers.difference(relations.keys()))

print("\n".join(sorted(sospects)))
