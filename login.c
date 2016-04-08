#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int i= 0;
char * entries[2]; // 1st entry is user name 2nd is password
int loginStatus=0;

//takes input an already parsed section, eg username=bob
int parser( char *s )
/* Nested strtoks are a problem so this is our own parser*/
{
	char *vname;
	char *val;

        //this part  gets rid of the CGI vatiabble name tag
	if(s == '\0') {
		printf("X_ERR='Null phrase'\n");
                i++; 
		return 1;
	}
	vname = s;//i we ll need the vname later on we can get it form here
	while( (*s != '\0')  && (*s != '=')) s++;
	if(*s == '\0' ) 
        {
		printf("X_ERR='Null assignment'\n");
                i++;
		return 1;
	}
	*(s++) = '\0';
       	//now the pointer points to the beggining of the username/password
    
        val =s;
        while( (*s != '\0')  && (*s != '=')) s++;
        *(s++) = '\0';
        entries[i]=val;
        i++;
        return 0;
        
        
}







int main(void)
{

 char *query_string=getenv("QUERY_STRING"); 
 char buffer[ strlen(query_string) +1];
 strcpy(buffer, query_string);



 char* token;

  token = strtok(buffer,"&");
  while(i<2) 
  {
    loginStatus=parser(token);
    token= strtok(NULL,"&");
  }
  

  //if user name,pasword is missing OR invalid username/pass
  if(loginStatus)
  {

   printf("%s%c%c\n","Content-Type:text/html",13,10);
   printf("<html>");

   printf("<head><title>ERROR</title></head>");
   printf("<body><p>Error Invalid Password</p></body>");
   printf("<P>HERE PUT LINK 1 TO HOME PAGE");
   printf("<P>HERE PUT LINK 2 BACK TO LOGIN PAGE");
   return 1;


  }



  FILE *in=fopen("indexxx.html", "rt"); //File pointer to the dashboard

  if(in == NULL) //give 404 Error if dashboard is missing
  {
  printf("%s%c%c\n","Content-Type:text/html",13,10);
  printf("<html>");

  printf("<head><title>ERROR</title></head>");
  printf("<body><p>Error 404 Dashboard Not Found</p></body>");
  printf("<P>Username is %s", entries[0]);
  printf("<P>Password is %s", entries[1]);
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
