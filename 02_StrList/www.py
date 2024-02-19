word = input()

a = word[3::7]
b = word[7::5]
c = str(int(a) + int(b) + 10000)
d = c[-4:-1]
e = (int(d[0]) + int(d[1]) + int(d[2]))%10 +1
f = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"][e-1]

print(d+f)