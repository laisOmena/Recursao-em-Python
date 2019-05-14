name = input("Digite seu nome: ")
name = name.split(" ")
i = 0
name2 = []
while i != len(name):
    name2.append(name[i][0])
    print(name2)
    i += 1
login = ""
for i in name2:
    login = login + i
print(login)