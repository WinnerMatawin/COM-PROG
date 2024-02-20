word = input()
ans = str()
for i in range(len(word)) :
    if word[i] == "(" :
        ans += "["
    elif word[i] == "[" :
        ans += "("
    elif word[i] == ")" :
        ans += "]"
    elif word[i] == "]" :
        ans += ")"
    else :
        ans += word[i]
print(ans)