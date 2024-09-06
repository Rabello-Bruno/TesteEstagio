string = input("Digite o texto a ser invertido: ")

string_invertida = ''

for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

print("Texto invertido:", string_invertida)
