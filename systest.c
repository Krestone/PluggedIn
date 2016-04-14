#include <stdio.h>
#include <stdlib.h>

//THIS SHOULD BE WRITTEN IN PYTHON

int main()
{

   FILE *in=fopen("index.html", "rt"); //File pointer to the dashboard
  //check if dashboard available
    if(in == NULL) //give 404 Error if dashboard is missing
   {
    printf("%s%c%c\n","Content-Type:text/html",13,10);
    printf("<html>");

    printf("<head><title>ERROR</title></head>");
    printf("<body><p>Error 404 Dashboard Not Found</p></body>");
   // printf("<P>Username is %s", entries[0]);
   // printf("<P>Password is %s", entries[1]);
    return 1;

   }

    //proceed to printing dashboard
    printf("%s%c%c\n","Content-Type:text/html",13,10);

    int c;
    c=fgetc(in);
    while(!feof(in) )
    {
     fputc(c, stdout);
     c=fgetc(in);
    }
    fclose(in);
    return 0;







}
