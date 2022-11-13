#include <stdio.h>

int fibo(int n);
int main(){
  int k = -1, r=-1;

    while(k < 0){
        printf("qual a posição de fibonacci você quer?\n(escolha um numero entre 0 e 45)\n");
        scanf("%d",&k);
        if(k < 0|| k > 45){
            printf("Valor inválido\n\n");
            k=-1;
        }
    }

    while(r < 0){
    printf("Qual método você quer usar?\n1 - iterativo\n2 - recursivo\n");
        int m;
        scanf("%d",&m);

        switch (m){
            case 1:// função iterativa
                int f = 0, g = 0, h = 0;
                for(int i = 0; i < k; i++) {
                    if(i == 1)h = 1;
                    else {
                        f = g;
                        g = h;
                        h = f + g;
                    }
                }
                r = g + h;
                break;
            case 2:// função recursiva
                r = fibo(k);
                break;
            default:
                printf("Valor inválido\n\n");
                break;
        }
    }

  printf ("o valor na posição [%d] da sequencia de fibonacci é [%d]\n", k, r);
  return 0;
}

int fibo(int n){
  if (n <= 0) return 0;
  else if (n == 1) return 1;
  else return fibo(n - 1) + fibo(n - 2);
}