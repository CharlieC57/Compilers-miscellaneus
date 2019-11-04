var [a-zA-z]+[a-zA-z0-9\-_]*
int [0-9]+
%%
{var} {printf("var valida");}
[-+]?{int} {printf("entero valido");}
[-+]?{int}\.{int} {printf("decimal valido");}
{int}\*\*{int} {printf("Potencia valida");}
{int}[+\-*/]{int}|mod({int}) {printf("operacion valida");}
