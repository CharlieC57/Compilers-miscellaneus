%{
  #include <math.h>
  #include <stdio.h>
%}
             
/* Declaraciones de BISON */
%union{
	int entero;
  float real;
}

%token <entero> ENTERO
%token <real> REAL
%token MOD
%type <entero> exp
%type <real> expr
             
%left '+' '-'
%left '*' '/'
             
/* Gramática */
%%
             
input:    /* cadena vacía */
        | input line             
;

line:     '\n'
        | exp '\n'  { printf ("\tresultado: %d\n", $1); }
;
             
exp:     ENTERO	{ $$ = $1; }
	| exp '+' exp        { $$ = $1 + $3;    }
	| exp '*' exp        { $$ = $1 * $3;	}
  | exp '-' exp         { $$ = $1 - $3;}
  | exp '/' exp       { $$ = $1 / $3;	}
  | MOD "(" ENTERO "," ENTERO ")" { $$ = $3 % $5;	}
;
expr:   REAL { $$ = $1;}
  | expr '+' expr        { $$ = $1 + $3;    }
	| expr '*' expr        { $$ = $1 * $3;	}
  | expr '-' expr         { $$ = $1 - $3;}
  | expr '/' expr       { $$ = $1 / $3;	}
             
%%

int main() {
  yyparse();
}
             
yyerror (char *s)
{
  printf ("--%s--\n", s);
}
            
int yywrap()  
{  
  return 1;  
}  
