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
%token VAR

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
        | expr '\n' { printf ("\tresultado: %f\n", $1); }
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
  | exp '+' expr        { $$ = $1 + $3;    }
	| exp '*' expr        { $$ = $1 * $3;	}
  | exp '-' expr         { $$ = $1 - $3;}
  | exp '/' expr       { $$ = $1 / $3;	}
  | expr '+' exp        { $$ = $1 + $3;    }
	| expr '*' exp        { $$ = $1 * $3;	}
  | expr '-' exp         { $$ = $1 - $3;}
  | expr '/' exp       { $$ = $1 / $3;	}
%%

int main() {
  yyparse();
  return 0;
}
             
void yyerror (char *s)
{
  printf ("--%s--\n", s);
}
            
int yywrap()  
{  
  return 1;  
}  
