def is_fibonacci(num):
    
    fib_1 = 0
    fib_2 = 1
    
    if num == fib_1 or num == fib_2:
        return True
    
    while fib_2 < num:
        fib_next = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_next
        if fib_2 == num:
            return True
    
    return False

numero = int(input("Digite um número: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
3
