var [a-zA-z]+[a-zA-z0-9]*
int -?[0-9]+
%%
{var} {printf("var valida");}
{int} {printf("entero valido");}
