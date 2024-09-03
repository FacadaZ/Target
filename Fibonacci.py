def pertence_fibonacci(n):
    a, b = 0, 1
    
    while b < n:
        a, b = b, a + b
    
    if b == n or n == 0:
        return f"o numero {n} pertence a sequencia de Fibonacci"
    else:
        return f"o numero {n} não pertence a sequencia de Fibonacci"

numero = int(input("Informe um numero: "))
resultado = pertence_fibonacci(numero)
print(resultado)
