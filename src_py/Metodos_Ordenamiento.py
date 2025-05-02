class MetodosOrdenamiento:
    def sortBubble(self, array):
        print("Este método implementaría Bubble Sort, pero solo imprime este mensaje.")

    def sort_burbuja_mejorado(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        while n > 0:
            nuevo_n = 0
            for i in range(1, n):
                if arreglo[i - 1] > arreglo[i]:
                    arreglo[i - 1], arreglo[i] = arreglo[i], arreglo[i - 1]
                    nuevo_n = i
            n = nuevo_n
        return arreglo

    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            indice_min = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[indice_min]:
                    indice_min = j
            arreglo[i], arreglo[indice_min] = arreglo[indice_min], arreglo[i]
        return arreglo

    def sort_shell(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2
        return arreglo

        

                