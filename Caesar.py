#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Metodo para desencriptar la palañbra con Mayusculas, espacios y Minusculas.
def desencriptar(text,shift):
    result = "" 
    #Bucle de longitud del texto para cubrir toda la frase
    for i in range(len(text)): 
        #se asigna a una variable las letras
        char = text[i] 
        #Si es mayuscula, ord(char) -> da el valor de la letra en ASCII, 65 -> valor de A en tabla ASCII, len(abc) -> longitud del abecedario
        if (char.isupper()): 
            result += chr((ord(char) + shift-65) % len(abc) + 65) 
        #Agrega un espacio cuando existe uno en el texto (para no omitirlos)
        elif(char.isspace() == True):
            result += " "
        #Agrega una coma cuando existe una en el texto (para no omitirlos)
        elif(ord(char) == 44):
            result += chr(44)
        #Agrega un punto cuando existe uno en el texto (para no omitirlos)
        elif(ord(char) == 46):
            result += chr(46)
        #Si es minuscula, ord(char) -> da el valor de la letra en ASCII, 97 -> valor de a en tabla ASCII, len(abc) -> longitud del abecedario
        else:
            result += chr((ord(char) + shift-97) % len(abc) + 97)
    return result 

#Metodo que cuenta las letras que se repiten en el texto en observacion. Se regresa el conteo de la frase en observación
def lista_Ori(text):
    #Se declaran e inician las variables locales
    lista_sumaOri = []
    counter = 0
    #Conteo de letras. Se utiliza la función append para ¡ncorporar los valores del conteo en una lista nueva
    for abd_div in abc:
        counter = text.count(abd_div)
        lista_sumaOri.append(counter)
    print(lista_sumaOri)
    return lista_sumaOri
    
#Metodo que cuenta las letras que se repiten en el texto estandar. No se regresa nada
def lista_Est(text):
    #Se declaran e inician las variables locales    
    lista_sumaEst = []
    counter = 0
    #Conteo de letras. Se utiliza la función append para ¡ncorporar los valores del conteo en una lista nueva.
    for abd_div in abc:
        counter = text.count(abd_div)
        lista_sumaEst.append(counter)
    fileText3.write(str(lista_sumaEst))
    fileText3.write("\n")
    ####print (lista_sumaEst)
    chiCuadrada(lista_sumaEst)

#Metodo que genera las tablas de frecuencias conforme al texto seleccionado (Genera ambos)
def tablasFrecuencias(text1, text2):
    #Se declaran e inician las variables locales
    j = 1
    #Llamada al método lista_Ori con el texto en Observación
    lista_Ori(txt1)
    #Bucle para recorrer el texto estandar 26 veces
    for j in range(26):
        result_Est = ""
        #Bucle para recorrer el texto con un desplazamiento de 1
        fileText3.write("Frase estándar con shift " + str(j+1) + ": ")
        for i in range(len(txt2)):
            char = txt2[i]
            if (char.isupper()): 
                result_Est += chr((ord(char) + j-65) % len(abc) + 65) 
            elif(char.isspace() == True):
                result_Est += " "
            else:
                result_Est += chr((ord(char) + j-97) % len(abc) + 97)
        #Llamada al método lista_Est con el texto Estándar
        lista_Est(result_Est)
        #print "\n"
    return 0

#Método para filtrar el texto estándar. 225 = á, 233 = é, 237 = í, 243 = ó, 250 = ñ, 242 = n
def filtrarTexto(texto):
    for i in texto:
        if(ord(i) == 225):
            texto = texto.replace(chr(ord(i)), "a")
        elif(ord(i) == 32):
            texto = texto.replace(chr(ord(i)), " ")
        elif(ord(i) == 44):
            texto = texto.replace(chr(ord(i)), ",")
        elif(ord(i) == 46):
            texto = texto.replace(chr(ord(i)), ".")
        elif(ord(i) == 233):
            texto = texto.replace(chr(ord(i)), "e")
        elif(ord(i) == 237):
            texto = texto.replace(chr(ord(i)), "i")
        elif(ord(i) == 243):
            texto = texto.replace(chr(ord(i)), "o")
        elif(ord(i) == 250):
            texto = texto.replace(chr(ord(i)), "u")
        elif(ord(i) == 241):
            texto = texto.replace(chr(ord(i)), "n")
        elif not((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
            texto = texto.replace(chr(ord(i)), "")
    return texto

#Método que genera la Chi^2
def chiCuadrada(lista_suma):
    #Se declaran e inician las variables locales
    sumaChi = 0
    #Bucle para obtener la proporción estándar, el residuo, el residuo al cuadrado y chi por cada letra. 
    for i in range(len(abc)):
        est = (float(lista_suma[i])/float(lenLorem))*float(lenEncrip)
        #print ("Estándar a proporción", est)
        res = lista_Ori(txt1)
        residuo = (float(res[i])-(float(est)))
        #print ("residuo", residuo)
        residuoCuadrado = residuo*residuo
        #print ("residuo cuadrado", residuoCuadrado)
        chi = (float(residuoCuadrado)/float(est))
        #fileText3.write("chi: " + str(chi))
        #fileText3.write("\n")
        sumaChi = sumaChi + chi
    #print sumaChi
    sumatoriaChi.append(sumaChi)
    fileText3.write("Chi cuadrada: " + str(sumaChi) + "\n\n\n")
    #print sumatoriaChi
    return 0

#Abecedario (texto con los carácteres deseados a que cuente)
abc = "abcdefghijklmnopqrstuvwyxz"

#Archivo del texto encriptado
fileText=open("Archivo.txt", "r")
if fileText.mode == 'r':
    txt1 =fileText.read() 

#Longitud del texto sin contar espacios.
lenEncrip = len(txt1.replace(" ", ""))
    
#Longitud del texto estándar
fileText2=open("Lorem.txt","r")
if fileText2.mode == 'r':
    txt2=fileText2.read()

filtrarTexto("áéíóú")

#Longitud del texto sin contar espacios
lenLorem = len(txt2.replace(" ", ""))

#Inicialización de la lista que genera la Chi^2
sumatoriaChi = []

#Menu
print (" ")
print ("¿Qué deseas hacer?")
print ("1) Descrifrar")
print ("2) Encriptar")
print (" ")
op = int(input(" "))
print (" ")

fileText3=open("Resultados.txt","a")
fileText3.seek(0)
fileText3.truncate()

#Operaciones del Menú
if(op == 2):
    a = input("Frase: ")
    texto = filtrarTexto(a)
    shift = int(input("Desplazamiento: "))
    print (" ")
    print ("Mensaje encriptado: " + desencriptar(texto,shift))
    print (" ")
    fileText3.close()
else: 
    print ("Mensaje encriptado: " + txt1)
    tablasFrecuencias(txt1, txt2)
    shift = sumatoriaChi.index(min(sumatoriaChi))*-1
    print ("Mensaje descifrado: " + desencriptar(txt1,shift))
    print (" ")
    fileText3.write("Mensaje encriptado: " + txt1 + "\n\n")
    fileText3.write("Los resultados fueron: \n")
    fileText3.write("Chi cuadrada más pequeña:  " + str(min(sumatoriaChi)) + "\n")
    fileText3.write("Ubicado en el index: " + str((shift-1)*-1) + "\n\n")
    fileText3.write("Mensaje descifrado: " + desencriptar(txt1,shift) + "\n\n")
