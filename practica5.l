%{
#include "ejemplo2.tab.h"
%}

NUM [0-9]+
VAR [a-zA-Z][a-zA-Z0-9]*
%%

{NUM}           {
		printf("Numero entero %s\n",yytext);
                yylval.entero = atoi(yytext);
                return (ENTERO);
                }
{NUM}\.{NUM}    {
		printf("Numero real(float) %s\n",yytext);
                yylval.entero = atof(yytext);
                return (REAL);
                }

"+"|"*"|"-"|"/"	{
		printf("Signo op\n");
                return (yytext[0]);
                }

"("|")"            {
		printf("Parentesis\n");
                return (yytext[0]);
                }
","            {
		printf("Coma\n");
                return (yytext[0]);
                }
";"             {
		        printf("Punto y coma\n");
                return (yytext[0]);
                }
"="             {
		        printf("Punto y coma\n");
                return (yytext[0]);
                }
[mM][oO][dD]    {
		printf("Modulo\n");
                return (MOD);
                }
"\n"            {
		printf("Salto de linea\n");
                return (yytext[0]);
                }
{VAR}           {
		        printf("Variable \n");
                return (VAR);
                }
%%
