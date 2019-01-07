#include <stdio.h>
void foo(int count, float** array, int size)
{
   int ii,jj;
   for (ii=0;ii<count;ii++){
      for (jj=0;jj<size;jj++)
         printf(" %f", array[ii][jj]);
   }
printf("\n");
}
