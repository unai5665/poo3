def decimal_a_romano(numero):
    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simbolos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    resultado = ""
    i = 0
    while numero > 0:
        for _ in range(numero // valores[i]):
            resultado += simbolos[i]
            numero -= valores[i]
        i += 1
    return resultado

def romano_a_decimal(romano):
    romano_valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    prev_val = 0
    for letra in romano:
        val = romano_valores[letra]
        decimal += val
        if prev_val < val:
            decimal -= 2 * prev_val
        prev_val = val
    return decimal


