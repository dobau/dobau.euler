public class Tres {

	public static void main(String[] args) {
		System.out.println(largestPrime(10));
	}

	public static boolean ehPrimo(long numero) {
		if (numero == 2) {
			return true;
		}

		if (numero % 2 == 0) {
			return false;
		}

		long limite = (long) (Math.sqrt(numero) + 1);
		for (long i = 3; i < limite; i += 2) {
			if (numero % i == 0) {
				return false;
			}
		}

		return true;
	}

	static long largestPrime(long n) {
		int i = 1;
		for(; n != i && i <= n; i++)
			if( n % i == 0 )
				n /= i;
		return n;
	}

}