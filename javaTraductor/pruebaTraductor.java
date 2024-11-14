public class pruebaTraductor {
    public static int operacion_basica(int a, int b, int c, int d, int e, int f) {
        int resultado;
        resultado = a*b+c/d*e+b-f;
        return resultado;
    }

    public static void main(String[] args) {
        System.out.println(operacion_basica(6, 6, 5, 4, 3, 2));
    }
}