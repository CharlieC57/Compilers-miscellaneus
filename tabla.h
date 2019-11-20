typedef struct sll
{
    char tipo;
    long long int valor;
    char* lex;
    int id;
    sll* sig;
}lista;

lista* search(int id,lista *t){
    while(t->sig!=NULL){
        if(t->sig->id==id)
            return t;
        else
            t=t->sig;
    }
    return t;
}

void insert(char* cad,lista *t){
    lista* nodo;
    int id;
    id=hasheo(cad);
    nodo=search(id,t);
}

int hasheo(char* cad){
    int hash=0,i=0;
    while(cad[i]!='\0'){
        hash+=cad[i]*i;
    }
    return hash;
}