def fibonacci(n):
    if n <= 1:
        return [0] * n
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq
def main():
    numero = int(input("Digite um numero: "))
    fib_seq = fibonacci(numero + 1)
    if numero in fib_seq:
        print(f"O numero {numero} pertence a sequencia de Fibonacci!")
    else:
        print(f"O numero {numero} nao pertence a sequencia de Fibonacci.")
if __name__ == "__main__":
    main()