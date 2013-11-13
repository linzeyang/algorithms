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


def fibonacci_recursive(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        previous = fibonacci_recursive(n - 1)
        previous.append(previous[-2] + previous[-1])
        return previous
