class NumerosRomanos:
    @staticmethod
    def entero_a_romano(numero):
        valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        simbolos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        resultado = ''
        indice = 0
        while numero > 0:
            if numero >= valores[indice]:
                resultado += simbolos[indice]
                numero -= valores[indice]
            else:
                indice += 1
        return resultado

    @staticmethod
    def romano_a_entero(romano):
        valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        anterior = 0
        longitud = len(romano)
        
        for i in range(longitud):
            valor = valores[romano[i]]
            if i < longitud - 1 and valor < valores[romano[i + 1]]:
                total -= valor
            else:
                total += valor
        
        return total

# Ejemplo de uso
if __name__ == '__main__':
    print(NumerosRomanos.entero_a_romano(500))   # Salida: D
    print(NumerosRomanos.romano_a_entero('IX'))  # Salida: 9
