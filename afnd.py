#!/usr/bin/python3.5

class estado:
    def __init__(self,nombre,alfabeto):
        self.id=nombre
        self.trancisiones=dict()
        for i in alfabeto:
            self.trancisiones[i]=["Error"]
    def addTrans(self,c,nestado):
        self.trancisiones[c].append(nestado)
        if self.id!="Error":
            try:
                if self.id!="Error":
                    index=self.trancisiones[c].index("Error")
                    self.trancisiones[c].pop(index)
            except Exception as e:
                print(e)
                pass
    def trans(self,c):
        return self.trancisiones[c]
class afn:
    def __init__(self, estados, alfabeto, inicial, finales, deltas):
        self.estados=dict()
        for i in estados:
            self.estados[i]=estado(i,alfabeto)
        self.estados["Error"]=estado("Error",alfabeto)
        for x in alfabeto:
            self.estados["Error"].addTrans(x,"Error")
        self.alfabeto = alfabeto
        self.actual=inicial[0]
        self.finales=finales
        for x in deltas:
            self.estados[x[0]].addTrans(x[1],x[2])
    def evaluar(self,cadena,index,actual,recorrido):
        if index>len(cadena)-1:
            if actual in self.finales:
                print(recorrido)
                print("aceptado")
        else:
            siguientes=self.estados[str(actual)].trans(cadena[index])
            for x in siguientes:
                anexo=recorrido.copy()
                anexo.append("P("+str(actual)+","+cadena[index]+")->"+str(x))
                self.evaluar(cadena,index+1,x,anexo)


#formato archivo:
#Q
#alfabeto
#S
#F
#delta
def lectura():
    datos=[]
    deltas=[]
    recorrido=[]
    nombre=input("Indique el nombre del archivo contenedor: ")
    with open(nombre, "r") as file:
        for i in range(4):
            linea = file.readline()
            linea = linea[:-1]
            datos.append(linea.split(','))
        trans=file.readlines()
        for i in trans:
            i=i[:-1]
            deltas.append(i.split(','))
    automata=afn(datos[0],datos[1],datos[2],datos[3],deltas)
    palabra=input("Introduzca una palabra a evaluar: ")
    automata.evaluar(palabra,0,automata.actual,recorrido)
    #print(automata.estados['0'].trancisiones)
    #print(automata.alfabeto)
    #print(automata.actual[0])
lectura()
