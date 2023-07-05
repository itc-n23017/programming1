def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return binary


decimal_number = 23
binary_number = decimal_to_binary(decimal_number)
print(binary_number)
