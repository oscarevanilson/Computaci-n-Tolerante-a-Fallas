#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define try bool __HadError=false;
#define catch(x) ExitJmp:if(__HadError)
#define throw(x) __HadError=true;goto ExitJmp;

int main(int argc, char *argv[])
{
    try
    {
        printf("Se imprime\n");
        throw();
        printf("No se imprime\n");
    }
    catch(...)
    {
        printf("Error con try-catch\n");
    }
    
	FILE *fout;

   if ((fout = fopen(argv[1], "w")) == NULL) {
      perror("Error con perror, no abre archivo");
      return EXIT_FAILURE;
   }
    return EXIT_SUCCESS; 
}
