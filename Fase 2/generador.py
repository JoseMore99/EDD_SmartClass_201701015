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

    
