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
		return 0;
	}
	vname = s;//i we ll need the vname later on we can get it form here
	while( (*s != '\0')  && (*s != '=')) s++;
	if(*s == '\0' ) 
        {
		printf("X_ERR='Null assignment'\n");
                i++;
		return 0;
	}
	*(s++) = '\0';
       	//now the pointer points to the beggining of the username/password
    
        val =s;
        while( (*s != '\0')  && (*s != '=')) s++;
        *(s++) = '\0';
        entries[i]=val;
        i++;
        return 1;
        
        
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
    parser(token);
    token= strtok(NULL,"&");
  }
  

  

  //validate password
  FILE *validate= fopen("users.txt", "rt"); //file pointer to database
  
  if(validate == NULL) //give Error if problem reading database
  {
    printf("%s%c%c\n","Content-Type:text/html",13,10);
    printf("<html>");
    printf("<head><title>ERROR 01001</title></head>");
    printf("<body><p>DATABASE NOT FOUND</p></body>");
    fclose(validate); //validation done
    return 1;

 }
 
  char field[50];
  fgets( field, 50, validate);
  field[strlen(field) - 1] = '\0'; //removes newline

  while(!feof(validate) ) 
  {
    if(strcmp(entries[0], field) == 0)//if user name is valid
    {
      fgets( field, 50, validate);
      field[strlen(field) - 1] = '\0';
      if( strcmp(entries[1], field) == 0)//if password is valid
      {
        loginStatus=1; //login is valid now
        break;
      }
      else
      {
      break;
      }
    }
    //skip 4 lines to next user name
    int c1=0;
    for(c1; c1<4; c1++)
    {  
      fgets( field, 50, validate);
      field[strlen(field) - 1] = '\0'; 
    }
  }
    

  fclose(validate); //validation done






  FILE *in=fopen("index.html", "rt"); //File pointer to the dashboard


 
  //publish dashboard to STDOUT character by character if valid login
  if(loginStatus)
  {
     system("./systtest.cgi"); //name of the python script to be called here    
  }
  else
  {  
   //if failure  
   printf("%s%c%c\n","Content-Type:text/html",13,10);
   printf("<html>");

   printf("<head><title>ERROR INVALID LOGIN!!!!!!! SHAM, QI DONT BE LAZY CREATE ACCOUNTS</title></head>");
   printf("<body><p>ERROR INVALID LOGIN!!!!!!! SHAM, QI DONT BE LAZY CREATE ACCOUNTS</p></body>");
   printf("<P>HERE PUT LINK 1 TO HOME PAGE");
   printf("<P>HERE PUT LINK 2 BACK TO LOGIN PAGE");
   return 1;
  }

   
}
