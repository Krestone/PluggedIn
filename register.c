#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int unique=1;
int i= 0;
char * entries[4]; // 1st entry is user name 2nd is password
int loginStatus=0;

//takes input an already parsed section, eg username=bob
int parser( char *s )
/* Nested strtoks are a problem so this is our own parser*/
{
        char *vname;
        char *val;
        char buf[3]; 
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
        while( (*s != '\0')  && (*s != '='))
        {
 	   s++;//next character 
	   switch( *s ) //fix URL encoding abnormalities
           {
			case '%':
				buf[0]=*(++s); buf[1]=*(++s); 
				buf[2]='\0';
				sscanf(buf,"%2x",s);
				break;
			case '+':
				*s = ' ';
				 unique=0;
                                 break;
           }
          
        }


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
  while(i<4)
  {
    loginStatus=parser(token);
    token= strtok(NULL,"&");
  }

  //Do no allow empty boxes
  int c2=0;
  for(c2; c2<4; c2++)
  {
    if(entries[c2] == NULL || *entries[c2] == '\0' )
    {
       unique=0;
       break;
    } 

  }


  FILE *out=fopen("users.txt", "a+");
  
  //check if unique
  char field[50];
  fgets( field, 50, out);
  field[strlen(field) - 1] = '\0'; //removes/n

  while(!feof(out) ) 
  {
    if(strcmp(entries[0], field) == 0)//if theyre same
    {
      unique=0;
      break;
    }
   
    int c1=0;
    for(c1; c1<4; c1++)
    {  
      fgets( field, 50, out);
      field[strlen(field) - 1] = '\0'; 
    }
    //we skip 4 lines to the username



  }



  //if unique user name and password append to database users.txt
  if(unique)
  {
    int counter=0;
    for(counter; counter<4; counter++)
    { 
       fputs(entries[counter], out);
       fputc('\n', out);
    }
  }
 
  //if succesfull register, generate link back to login page
  if(unique)
  {
     FILE *suc=fopen("registerSucess.html", "rt");
     printf("%s%c%c\n","Content-Type:text/html",13,10);
     int c;
      c=fgetc(suc);
      while(!feof(suc) )
      {
       fputc(c, stdout);
       c=fgetc(suc);
      }

    fclose(out);
    fclose(suc);
    return 0;
  }

   //if problem
   FILE *error=fopen("registerError.html", "rt");
   printf("%s%c%c\n","Content-Type:text/html",13,10); 
   int c;
      c=fgetc(error);
      while(!feof(error) )
      {
       fputc(c, stdout);
       c=fgetc(error);
      }
    
    fclose(out);
    fclose(error);
    return 1;



}
