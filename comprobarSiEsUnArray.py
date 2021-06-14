# array_numeros=[1,2,3,4,5,99,77,65,10,11,22]
# print('array estandar',array_numeros)
# for item in range(0,len(array_numeros)):
#     if(array_numeros[item]%2==0):
#         array_numeros[item]='PAR'

# # recorremos y lo imprimimos
# print()
# # for item in array_numeros:
# #     print(item)

# # o solo lo imprimimos
# print('array modificando ',array_numeros)

# print()
# def lista(argumento):
#     if(type(argumento)==int):
#         print('no es array')
#         print(argumento)
#     else:
#         print('es array')
#         print(argumento)
# lista(1)

import re
name=str(input('ingrese su nombre'))
password=input('ingrese su pasword')
def validarClave(clave):
    contador=0
    while(contador!=1):
        if(len(clave)>=6 and len(clave)<=12):
            if(re.search('[a-z]',clave) and re.search('[a-z]',clave)):
                if(re.search('[0-9]',clave)):
                    contador=1
                    return print('registro exitoso')
        clave=input('ingrese bien el contrasenia')
        contador=0
    return print('debe ingresar bien la contraseia')
            
validarClave(password)
# lista1=[1,2,44,55]
# lista2=[3,2,64,75]
# lista3=[11,22,44,95]

arrayNuevo=[]
arrayNuevo.extend(lista1)
arrayNuevo.extend(lista2)
arrayNuevo.extend(lista3)
print(max(arrayNuevo))






