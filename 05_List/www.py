allgrade = ['F','D', '''D+''', 'C', 'C+', 'B', 'B+', 'A']
ids,grade = [],[]
x = input().split()
while x != ['q'] :
    ids.append(x[0])
    grade.append(x[1])
    x = input().split()
uids = input().split()

for i in uids:
    grade[ids.index(i)] = allgrade[min(7,allgrade.index(grade[ids.index(i)])+1)]
for i in range(len(ids)):
    print(ids[i], grade[i])
