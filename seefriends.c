#include <stdio.h>
#include <stdlib.h>

char *entries[1];
char *friends[500];
int friendNumber=0;
int i=0;

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


int main()
{

  char *query_string=getenv("QUERY_STRING");
  char buffer[ strlen(query_string) +1];
  strcpy(buffer, query_string);

  char* token;

  token = strtok(buffer,"&");
  parser(token);
  // now entries[0] is the username

  FILE *validate=fopen("users.txt", "rt");
 
  char field[50];//each line in users.txt
  fgets( field, 50, validate);
  field[strlen(field) - 1] = '\0'; //removes newline
  
  while(!feof(validate) )
  {
    char *username;
    username=strtok(field," ");
    if( strcmp(entries[0], username) == 0) //if user name is found
    {
      char *friend;
      friend = strtok(NULL," "); //get friend
      while( friend != NULL)
      {
      *(friends+friendNumber)=friend;
       friendNumber++;  
       friend = strtok(NULL," ");
      }
      *(friends+friendNumber)='\0';
      break;
    }
  
    //skip 4 lines to next user name line
    int c1=0;
    for(c1; c1<4; c1++)
    {
      fgets( field, 50, validate);
      field[strlen(field) - 1] = '\0';
    }
  }

  int index=0;
  printf("%s%c%c\n","Content-Type:text/html",13,10);
         printf("<html>");

         printf("<head><title>ERROR</title></head>");
         printf("<body><p>Error 404 Dashboard Not Found</p></body>");

  for(index; index<friendNumber; index++)
  {
    printf("<body><p>%s</p></body>", friends[index]);

  } 






  return 0;

}
