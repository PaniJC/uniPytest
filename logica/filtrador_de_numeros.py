class Filtrador:
    def filtrar_numeros(self,numeros, par):
        if par:
            return [num for num in numeros if num % 2 == 0]
        else:
            return [num for num in numeros if num % 2 != 0]