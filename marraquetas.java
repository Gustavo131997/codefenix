import java.util.Scanner;
class Main {

	public static void main(String[] args){
		Scanner leer = new Scanner(System.in);
		int cantPedidada;
		cantPedida = leer.nextInt();
		double result = cantPedidada/2;
		if (cantPedida%2 != 0){
			result++;

		}
		System.out.println((int)result);
	}

}
