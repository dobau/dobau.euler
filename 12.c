#include <stdio.h>

int conta_fatores(int n);

int main() {
    int found = 0;
    int r = 1;
    int triangulo = 1;
    int fatores = 0;
    
    while (!found) {
      triangulo = (r * (r + 1))/2;
      
      fatores = conta_fatores(triangulo);
      if (fatores > 500)
        found = 1;
      else
        r += 1;
        
        printf("%d = %d\n", triangulo, fatores);
    }
    
    return 0;
}

int conta_fatores(int n) {
 int count = 0;
  
  int i;
  for (i = 1; i <= n; i++) {
    if (n%i == 0) {
      count += 1;
    }
  }

  return count;
}
