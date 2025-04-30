import java.util.Random;

public class Benchmarking {
    
    private MetodosOrdenamiento mOrdenamiento;

    public Benchmarking(){
        long curentMills = System.currentTimeMillis();
        long currentNano = System.nanoTime();

        System.out.println("Current time: " + curentMills);
        System.out.println("Current time: " + currentNano);

        mOrdenamiento = new MetodosOrdenamiento();

        int[] arreglo = generarArregloAleatorio(1000000);

        Runnable  tarea= ()-> mOrdenamiento.burbujaTradicional(arreglo);

        double tiempoDuracionMillis = medirConCurentTimeMiles(tarea);
        double tiempoDuracionNanos = medirConCurentNano(tarea);

        System.out.println("Tiempo duracion millis: " + tiempoDuracionMillis);
        System.out.println("Tiempo duracion nanos: " + tiempoDuracionNanos);


    }

    private int[] generarArregloAleatorio(int tamaño){
        int[] Array = new int[tamaño];
        Random random = new Random();
        for(int i = 0; i< tamaño; i++ ){
            Array[i] = random.nextInt(1000000);
            System.out.println(Array[i]);
        }

        return new int[]{};
    }


    public double medirConCurentTimeMiles(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return  (fin - inicio) / 1000.0;
    }


    public double medirConCurentNano(Runnable tarea){
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }


}
