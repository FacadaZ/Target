def verifica_string(texto):
    contador = texto.lower().count('a')
    
    if contador > 0:
        return f"a letra 'a' aparece {contador} vezes na texto"
    else:
        return "a letra 'a' não aparece no texto"

texto = input("Informe uma string")
resultado = verifica_string(texto)
print(resultado)
