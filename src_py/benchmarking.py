from Metodos_Ordenamiento import MetodosOrdenamiento
import random
import time
class Benchmarking:
    def __init__(self):
        print('Benchmarking instanciado')

        self.mO = MetodosOrdenamiento()
        arreglo = self.build_arreglo(50000) 

        tarea = lambda: self.mO.sortBubble(arreglo)
        tarea2 = lambda: self.mO.sort_burbuja_mejorado(arreglo)
        tarea3 = lambda: self.mO.sort_seleccion(arreglo)
        
        #tiempoMillies = self.contar_con_current_time_millies(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)
        tiempoNano2 = self.contar_con_nano_time(tarea2)
        tiempoNano3 = self.contar_con_nano_time(tarea3)
       
        #print(f'Tiempo tiempo millies: {tiempoMillies}')
        print(f'Tiempo con tiempo nano burbuja: {tiempoNano}')
        print(f'Tiempo con tiempo nano burbujaMejorado: {tiempoNano2}')
        print(f'Tiempo con tiempo nano seleccion: {tiempoNano3}')


    def build_arreglo(self, tamano):
        arreglo = []
        for _ in range(tamano):
            numero = random.randint(0, 99999)
            arreglo.append(numero)
        return arreglo

        
    def contar_con_current_time_millies(self, tarea):
        inicio= time.time()
        tarea()
        fin = time.time()
        return(fin - inicio)

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return(fin - inicio) / 1_000_000_000.0

