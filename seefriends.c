#include <stdio.h>
#include <stdlib.h>

char *entries[1];//the username
char *friends[500];//the friends
int friendNumber=0;//number of friends
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


  //proceed to printing the html page
  //static html top
  FILE *htmlTop=fopen("seefriendsTop.html", "rt");
  printf("%s%c%c\n","Content-Type:text/html",13,10);
  int c;
      c=fgetc(htmlTop);
      while(!feof(htmlTop) )
      {
       fputc(c, stdout);
       c=fgetc(htmlTop);
      }

    fclose(htmlTop);

   //submit button cgi
   printf("<form name=\"seeuser\" action=\"http://www.cs.mcgill.ca/~shossa15/cgi-bin/displayuser.py\" method=\"get\">"); 
   printf("<input type=\"hidden\" name = \"username\" value=\"%s\">", entries[0]);
   

  //the dynamic part of the html that will be changed according to friends
   
   int index=0;
   for(index; index<friendNumber; index++)
   {
    printf("<div class=\"check\"><input type=\"radio\" name=\"friend\" value=\"%s\"></div>", friends[index] );
    printf("<div class=\"username\"><h2>%s</h2></div>", friends[index]);
   }



  //print static html bottom1
  FILE *htmlBot1= fopen("seefriendsBottom1.html", "rt");
      c=fgetc(htmlBot1);
      while(!feof(htmlBot1) )
      {
       fputc(c, stdout);
       c=fgetc(htmlBot1);
      }

    fclose(htmlBot1);

  //print topmenu javascript and hiddenfield connections to other pages
  
  printf("<form name=\"makefriend\" action=\"http://www.cs.mcgill.ca/~shossa15/cgi-bin/makefriends.py\" method=\"get\">");
  printf("<input type=\"hidden\" name = \"username\" value=\"%s\"> </form>" , entries[0]);

   printf("<form name=\"seefriend\" action=\"\" method=\"get\">");
   printf("<input type=\"hidden\" name = \"username\" value=\"%s\"></form>", entries[0]);
    
    printf("<form name=\"statusupdate\" action=\"http://www.cs.mcgill.ca/~ycukra/cgi-bin/status.py\" method=\"get\">");
    printf("<input type=\"hidden\" name = \"update\" value=\"\"><input type=\"hidden\" name = \"username\" value=\"%s\"></form>", entries[0]);


  //print static html bottom2
  FILE *htmlBot2=fopen("seefriendsBottom2.html", "rt");
      c=fgetc(htmlBot2);
      while(!feof(htmlBot2) )
      {
       fputc(c, stdout);
       c=fgetc(htmlBot2);
      }

    fclose(htmlBot2);

   
    






  return 0;

}
