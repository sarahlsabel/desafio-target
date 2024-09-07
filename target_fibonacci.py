def is_fibonacci(a):
    if a == 0:
        return True
    last_fibonacci = 0
    fibonacci = 1
    while a >= fibonacci:
        if a == fibonacci:
            return True
        next_fibonacci = fibonacci + last_fibonacci
        last_fibonacci = fibonacci
        fibonacci = next_fibonacci
        print(fibonacci)
    return False

def main():
    n = int(input("Escolha um número: "))
    if is_fibonacci(n):
        print("Esse número faz parte da sequência de fibonacci.")
    else:
        print("Esse número não faz parte da sequência de fibonacci.")
        

if __name__ == "__main__":
    main()