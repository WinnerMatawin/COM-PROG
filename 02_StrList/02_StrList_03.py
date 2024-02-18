dmy = input().split("/")
print(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][int(dmy[1])-1], end = " ")
print(dmy[0]+",", dmy[2])
