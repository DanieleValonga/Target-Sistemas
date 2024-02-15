def inverter_string(string):
    string_invertida = ""
    for i in range(len(string)-1, -1, -1):
        string_invertida += string[i]
    return string_invertida

string = "Ola, mundo!"

string_invertida = inverter_string(string)

print(string_invertida)
