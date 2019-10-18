#!/usr/bin/python3.5
import threading
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
            except:
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
    def evaluar(self,cadena,index,actual,recorrido,error):
        if index>len(cadena)-1:
                try:
                    siguientes=self.estados[str(actual)].trans("E")
                    for x in siguientes:
                        anexo=recorrido.copy()
                        anexo.append("P("+str(actual)+",E)->"+str(x))
                        hilo=threading.Thread(target=self.evaluar, args=(cadena,index,x,anexo,error))
                        hilo.start()
                except:
                    if actual in self.finales:
                        print("aceptado")
                        print(recorrido)
                        if len(error)>0:
                            print("Errores manejados:")
                            for e in error:
                                print(e)

        else:
            if cadena[index] in self.alfabeto:
                try:
                    siguientes=self.estados[str(actual)].trans("E")
                    for x in siguientes:
                        anexo=recorrido.copy()
                        anexo.append("P("+str(actual)+",E)->"+str(x))
                        hilo=threading.Thread(target=self.evaluar, args=(cadena,index,x,anexo,error))
                        hilo.start()
                except:
                    siguientes=self.estados[str(actual)].trans(cadena[index])
                    for x in siguientes:
                        anexo=recorrido.copy()
                        anexo.append("P("+str(actual)+","+cadena[index]+")->"+str(x))
                        hilo=threading.Thread(target=self.evaluar, args=(cadena,index+1,x,anexo,error))
                        hilo.start()
            else:
                maserror=error.copy()
                maserror.append("P("+str(actual)+","+cadena[index]+")")
                hilo=threading.Thread(target=self.evaluar, args=(cadena,index+1,actual,recorrido,maserror))
                hilo.start()
  


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
    error=[]
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
    automata.evaluar(palabra,0,automata.actual,recorrido,error)
    #print(automata.estados['0'].trancisiones)
    #print(automata.alfabeto)
    #print(automata.actual[0])
lectura()
