from db import *

def pegarValores(inputs,v0):
    todosInputs = []
    for i in inputs:
        todosInputs.append(i.get().lower())
    selecionado = v0.get()
    todosInputs.append(selecionado)
    return todosInputs

def moldarValores(y):
    itens = ''  
    for i in y:
        try:
            int(y[1])
        except:
            return False
        if len(str(i)) == 0 or y[-1] == 0:
            return False
    for i in y:        
        if y.index(i) != len(y)-1:
            itens += str(i) + "|"
        else:
            itens += str(i) + "\n"
    return itens 
 




def enviar(inputs,v0):
    values = pegarValores(inputs,v0)
    valores = moldarValores(values)
    if valores == False:
        return False
    else:    
        escrever(valores)
        leitura = ler()
        return leitura



def leitura(valor):
    albuns = ler()
    artistas = []
    for i in albuns:
       if valor in i[2].lower():
            if i[2] not in artistas:
                artistas.append(i[2])
            else:
                continue
    return artistas




def LerAnos(valueText,valueRadio):
    albuns = ler()
    Albuns = []
    for i in albuns:
        try:
            if valueRadio == "Antes" and int(valueText) >= int(i[1]):
                Albuns.append(i[0])
            else:
                if valueRadio == "Depois" and int(valueText) <= int(i[1]):
                    Albuns.append(i[0])   
        except:
            return False  
    return Albuns



            
    
    

    