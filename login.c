#include <stdio.h>
#include <stdlib.h>
int main(void)
{

 
 FILE *in=fopen("index.html", "rt"); //File pointer to the dashboard

 if(in == NULL) //give 404 Error if dashboard is missing
 {
 printf("%s%c%c\n","Content-Type:text/html",13,10);
 printf("<html>");

 printf("<head><title>ERROR</title></head>");
 printf("<body><p>Error 404 Dashboard Not Found</p></body>");
 return 1;

 } 
 

 //publish dashboard to STDOUT character by character

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
