import os 

def grafAVL(raiz,archi):
    if raiz:
        
        val = str(raiz.id)+"\\n"+str(raiz.estu.nombre)
        archi.write('"{}"[label="{}"];\n'.format(str(hash(raiz)),val))

        if raiz.izq.raiz != None:
            archi.write('"{}" -> "{}";\n'.format(str(hash(raiz)),str(hash(raiz.izq.raiz))))
        if raiz.der.raiz != None:
            archi.write('"{}" -> "{}";\n'.format(str(hash(raiz)), str(hash(raiz.der.raiz))))

        grafAVL(raiz.izq.raiz, archi)
        grafAVL(raiz.der.raiz, archi)

def grafB(raiz):
    archi = open("ArbolB.dot","w")
    archi.write("digraph G\n{\nnode[shape = record, height= .1];\n")
    graficandoB(raiz,archi)
    archi.write("}")
    archi.close()
    os.system("dot -Tpng  ArbolB.dot -o grafoB.png")

def graficandoB(raiz,archi):
    print(raiz.valores)
    label = "<"+str(hash(raiz.hijos[0]))+">"
    for i in range(raiz.contador):
        label+="|"+str(raiz.valores[i+1].codigo)+"\\n"+str(raiz.valores[i+1].nombre)+"|"
        label+="<"+str(hash(raiz.hijos[i+1]))+">"
    archi.write('"{}"[label="{}"];\n'.format(str(hash(raiz.valores[1])),label))
    for i in raiz.hijos:
        if i == None:
            continue
        archi.write('{}:{}->{}\n'.format(str(hash(raiz.valores[1])),hash(i),hash(i.valores[1])))
        graficandoB(i,archi)

    
