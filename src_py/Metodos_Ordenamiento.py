##Cree una clase MetodosOrdenamiento
# Crear un metodo sort Bubble que reciaba un arreglos el metodo solo imprima un mensaje

class MetodosOrdenamiento:
    def sortBubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n ):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo
    
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
            min = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min]:
                    min = j
            arreglo[i], arreglo[min] = arreglo[min], arreglo[i]
        return arreglo
    
    def sort_shell(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        while   n > 1:
            for i in range(n // 2):
               temp = arreglo[i]
               j = i 
               while j > n and arreglo[j - n] > temp:
                   arreglo[j] = arreglo[j - n]
                   j -= n
                   arreglo[j] = temp
                   n = n // 2

        

                