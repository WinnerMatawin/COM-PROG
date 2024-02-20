find = input()
word = input()
out = str()
n = 0
for c in word :
    if c in "\"(),.'" :
        out += ' '
    else :
        out += c
for w in out.split() :
    if w == find  :
        n += 1
print(n)
print(out)