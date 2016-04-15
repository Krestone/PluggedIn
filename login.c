#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int i= 0;
char * entries[2]; // 1st entry is user name 2nd is password
int loginStatus=0;
char command[50];
//prepare the commandline call line which in "./scriptName UserName" format(note the space inbetween)
char *commandParser()
{
    //prepare the commandline call line which in "./scriptName UserName" format(note the space inbetween)
    char argument[50];

    char *nameWithSpace =(char *)malloc( strlen(entries[0]) + 2 );
   *(nameWithSpace)=' ';
    char * counterPointer= nameWithSpace;
    counterPointer++;
   //we are going to insert a space before the username
    int i=0;
    for(i; i <  strlen(entries[0]);  i++ )
   {
     *(counterPointer++)=*(entries[0]+i);

   }

   *(counterPointer)='\0';




   strcpy(argument, nameWithSpace);
   strcpy(command, "./dashboard.py");
   strcat(command,argument);
   //command line command now in corect





    return command;

}



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

    return 1;

 }
 
  char field[50];
  fgets( field, 50, validate);
  field[strlen(field) - 1] = '\0'; 
  char *usr;
  usr=field; 
  strtok(usr," ");  
  
  while(!feof(validate) ) 
  {
    if(strcmp(entries[0], usr) == 0)//if user name is valid
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
      usr=field; 
      strtok(usr," "); 
    }
  }
    

  fclose(validate); //validation done




  FILE *in=fopen("index.html", "rt"); //File pointer to the dashboard


 
  //publish dashboard to STDOUT character by character if valid login
  if(loginStatus)
  {
       char *parsedCommand = commandParser(); //fromat commandline input
       system(parsedCommand); //we are calling dashboard.py here   
  
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
