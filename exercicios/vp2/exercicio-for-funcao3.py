# Crie uma funcao que recebe um texto
# e retorna verdadeiro, caso ele seja palindromo
# ou falso, caso não seja palindromo
# Teste a funcao ao final do codigo

def ehPalindromo(texto) :
    textoAoContrario = ""

    for letra in texto:
        textoAoContrario = letra + textoAoContrario

    if texto == textoAoContrario:
        return True
    else:
        return False

print(ehPalindromo("omo"))
print(ehPalindromo("apos a sopa"))
print(ehPalindromo("a sacada da casa"))