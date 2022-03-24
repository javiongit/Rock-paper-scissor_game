# El jugador escoge piedra, papel o tijera, la maquina hace una eleccion random entre estas 3
# y quien llegue a 3 puntos gana

import random
i=0
j=0
while i<3 and j<3:
    x=input("Escoge piedra,papel o tijera  ")
    print(x)
    if x=="piedra" or x=="papel" or x=="tijera":
        print("Buena eleccion")
        y=["piedra","papel","tijera"]
        w=random.choice(y)
        print('Yo escojo '+w)
        if (x=="piedra" and w=="tijera")or(x=="tijera" and w=="papel")or(x=="papel" and w=="piedra"):
            i+=1
            print("El resultado es {} a {}".format(i,j))
        elif (x=="piedra"and w=="papel")or(x=="papel" and w=="tijera")or(x=="piedra" and w=="papel"):
            j+=1
            print("El resultado es {} a {}".format(i,j))
        else:
            print('Ni para ti ni para mi')
            print("El resultado es {} a {}".format(i,j))

    else:
        print("Por favor escoja piedra, papel o tijera")
