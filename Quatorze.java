import java.util.*;

public class Quatorze {
    
    private static long next(long n) {
        if (n%2 == 0) {
            return n/2;
        } else {
            return 3*n + 1;
        }
    }
    
    public static void main(String[] args) {
        long maiorNumero = 0;
        long maiorCount = 0;
        
        for (long i = 1000000;i > 0;i--) {
            long next = i;
            long count = 0;
            
            while (next > 1) {
                count++;
                next = next(next);
            }

            count++;
            
            if (maiorCount < count) {
                maiorCount = count;
                maiorNumero = i;
            }
        }
        
        System.out.printf("%d = %d\n", maiorNumero, maiorCount);
    }
    
    
    
}