# pessoa1 = ["Eduardo", "23423423", "edumendes@gmail.com"]
# print(pessoa1[0], "\npossui CPF: ", pessoa1[1])

p1 = {'nome': 'Eduardo', 'cpf': '2309234234', 'email':'edumendes@gmail.com' }
p2 = {'nome': 'Eduardo1', 'cpf': '2309234234', 'email':'edumendes@gmail.com' }
p3 = {'nome': 'Eduardo2', 'cpf': '2309234234', 'email':'edumendes@gmail.com' }
p4 = {'nome': 'Eduardo3', 'cpf': '2309234234', 'email':'edumendes@gmail.com' }
p5 = {'nome': 'Eduardo4', 'cpf': '2309234234', 'email':'edumendes@gmail.com' }
p6 = {'nome': 'Eduardo5', 'cpf': '2309234234', 'email':'edumendes@gmail.com' }
p7 = {'nome': 'Eduardo6', 'cpf': '2309234234', 'email':'edumendes@gmail.com' }

print(p1['nome'], p1['cpf'], p1['cpf'], p1['email'])

pessoas = []
pessoas.append(p1)
pessoas.append(p2)
pessoas.append(p3)
pessoas.append(p4)
pessoas.append(p5)
pessoas.append(p6)
pessoas.append(p7)

# print(pessoas)
for pessoa in pessoas:
    print(pessoa['nome'], pessoa['cpf'], pessoa['email'])