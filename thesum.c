#include <stdio.h>

int main(){
 int num1=0, num2, ris=0;
 FILE *f;
  
 f = fopen("sum.dat", "r");

 if(!f) 
   printf("Il file sumdat non esiste e verra' creato automaticamente.\n");
 

 else{
   printf("Lettura dal file sum.dat...\n");
   printf("Acquisisco il valore da sum.dat...\n");
   fscanf(f,"%d", &num1);
   fclose(f);
} 

 printf("Il valore letto e': %d\n",num1);

 printf("Inserisci il numero da sommare: ");
 scanf("%d", &num2);
 ris = num1+num2;

 printf("Nuovo valore: %d\n",ris);
 printf("Salvataggio in sum.dat in corso...\n");
 f = fopen("sum.dat", "w");
 fprintf(f,"%d\n", ris); 
 fclose(f);
 

return 0;
}
