# def is_prime(n):
#     """Determina si un número entero es primo."""
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     elif n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def fibonacci(n):
#     """Devuelve el número Fibonacci correspondiente a la posición n."""
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
