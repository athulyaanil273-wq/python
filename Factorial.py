def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("How many numbers? "))
for i in range(1, n + 1):
    print(f"factorial({i}) = {factorial(i)}")
