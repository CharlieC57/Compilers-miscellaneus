var [a-zA-z]+[a-zA-z0-9_]*
int [0-9]+
denom [1-9][0-9]*
dec {int}\.{int}
num {int}|{dec}
%%
[a-zA-z]+("-")*/[a-zA-z0-9_]* {printf("var valida");}
[-+]?{int} {printf("entero valido");}
[-+]?{dec} {printf("decimal valido");}
{num}\*\*{int} {printf("Potencia valida");}
{num}"/"{denom} {printf("division valida");}
{num}[+\-*]{num}|mod({int}) {printf("operacion valida");}
