class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

p1 = Pessoa("Eduardo", "230492309", "edumendes@gmail.com")
p2 = Pessoa("Mairton", "230492309", "mairton@gmail.com")
p3 = Pessoa("joao", "230492309", "joao@gmail.com")
p4 = Pessoa("Adamor", "230492309", "adamor@gmail.com")

print(p1.nome, p1.cpf, p1.email)

pessoas = []

pessoas.append(p1)
pessoas.append(p2)
pessoas.append(p3)
pessoas.append(p4)
decisao = "S"

while (decisao == "S"):
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu cpf: ')
    email = input('Digite seu email: ')

    novaPessoa = Pessoa(nome, cpf, email)
    pessoas.append(novaPessoa)

    decisao = input("Deseja continuar, digite S para sim: ")

for p in pessoas:
    print(p.nome, p.cpf, p.email)
