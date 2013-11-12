#Algorithms for mathematical problems

def factorial_normal(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        product = 1

        for i in range(n, 1, -1):
            product *= i

        return product


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

