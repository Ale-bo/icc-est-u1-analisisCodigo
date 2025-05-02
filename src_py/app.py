import benchmarking as bM
#from benchmarking import Benchmarking 
from Metodos_Ordenamiento import MetodosOrdenamiento
#Archivo Principal o main
if __name__ == "__main__":
    print("Funciona")
    bench = bM.Benchmarking()
    metodosO = MetodosOrdenamiento()

    #tam = 10000
    tamanios = [5000, 10000, 20000]


    resultados = []

    for tam in tamanios:

        arreglo_base = bench.build_arreglo(tam)

        metodos_dic = {
        "burbuja": metodosO.sortBubble,
        "burbujaMejorado": metodosO.sort_burbuja_mejorado,
        "seleccion": metodosO.sort_seleccion,
        "shell": metodosO.sort_shell
        }

        for nombre, fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)

        for tam, nombre, tiempo_resultado in resultados:
            print(f'Tamano: {tam}, Metodo: {nombre}, Tiempo: {tiempo_resultado:.6f} segundos')




    
