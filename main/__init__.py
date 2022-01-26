"""
author = "Natalia Pérez Romero"
version = "1.0"
"""
import hashlib
import secrets
import struct

from Crypto.Cipher import AES
from getpass import getpass
from .reader_writer import read_txt,write_txt


# Algoritmo de Horner
# Recibe x el punto del domino en el que se va evaluar 
# n es el número de coeficientes
# coef es el arreglo de coeficientes
def horner_algorithm(x, n,coef):
    result = 0
    i=n-1
    while(i >= 0):
        result = (result * x) +coef[i]
        i = i-1
    return result


# Recibe el grado del polinomio, es 
# decir cuanto coeficientes elegir
# y la variable independiente k
def generate_coefficients(re,k):
    coe = [k]
    for i in range(1,re):
        coe.append(secrets.randbelow(k)+1)
    return coe

# Genera una lista con la forma [x,f(x)]
# Recibe:
# n el numero de coeficientes
# t el numero se evaluaciones requeridas
# k la variable independiente
# coef el arrevlo de coeficientes  
def generate_evaluations(n,t,k,coef):
    evaluations = []
    for i in range(t):
        x = secrets.randbelow(k)+1
        value = horner_algorithm(x,n,coef)
        tmp = str(x)+","+str(value)
        evaluations.append(tmp)
    return evaluations

# Recibe una lista con x,f(x)
# Evalua el polinomio P(0)
# Regresa k
def lagrange_polynomial(nlist):
    i = 0
    j = 0
    tmp = 1
    result = 0
    while(i < len(nlist)):
        if(j==len(nlist)): 
            j = 0
            tmp = 1
        while(j < len(nlist)):
            if(i != j):
                x_i = int(nlist[i][0])
                x_j = int(nlist[j][0])
                subtraction = x_i-x_j
                tmp = (-x_j / (subtraction))*tmp  
            j=j+1
        
        fx = int(nlist[i][1])
        a = tmp * fx
        result = result + a
        i=i+1
        
    return result
            
    

# Se encarga de recibir la entrada y cifrar lo pedido
def cypher():
    try:
        file = str(input())   # Archivo para guarda n evaluaciones del polinomio
        n = int(input())  # num total de evaluaciones requeridas n>2
        t = int(input())   # num minimo de puntos necesarios para decifrar 1<t<n
        clean_file = str(input()) # nombre del archivo con el documento claro
        
        if(n>2 and t>1 and t<n):
            print("Contraseña: ")
            password = str(getpass()).encode('utf-8').strip()
            h = hashlib.sha256(password).hexdigest()
            k = int(h,16)
            
            key = hashlib.sha256(password).digest()
            
            coefficients = generate_coefficients(n,k) # Grado del polinomio
            
            ev = generate_evaluations(n,t,k,coefficients) # lista
            
            str_ev = "\n".join(str(i) for i in ev)
            write_txt("output/"+file+".frg",str_ev) # Crea el archivo con t evaluaciones
        
            texto = read_txt(clean_file)
            data = texto.encode("utf-8")
            cipher = AES.new(key,AES.MODE_EAX)
            nonce = cipher.nonce
            ciphertext,tag = cipher.encrypt_and_digest(data)
            
            ciphertext = ciphertext.hex()
            
            status = write_txt("output/"+clean_file+".aes",str(ciphertext))
            if(status): print("Se crearon los archivo")
        else:
            print("Valores invalidos")
    except FileNotFoundError:
        print("")
    except ValueError:
        print("Verifica la entrada")
    except Exception:
        print("Error inesperado")
    

# Se encarga de recibir la entrada y descifrar lo pedido 
def decipher():
    try:
        evaluations_file = str(input()) # archivo con t de las n evaluaciones de polinomio
        encrypted_file = str(input()) # nombre del archivo cifrado
        
        ciphertext = read_txt(encrypted_file)
        
        ev = read_txt(evaluations_file)
        evlist = ev.split("\n")
        nlist=[]
        for e in evlist:
            t = e.split(",")
            nlist.append(t)
            
        float_key = lagrange_polynomial(nlist)
        
        key = struct.pack('d',float_key)
        tmp = key.zfill(16)
        
        cipher = AES.new(tmp, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext=bytes.fromhex(ciphertext)
        texto_plano = cipher.decrypt(ciphertext)
        # Problemas para pasar de bytes a cadena str(texto_plano,'utf-8') no funciona
        # Tampoco texto_plano.decode('utf-8')
        write_txt("output/"+encrypted_file+".txt",str(texto_plano))
    except FileNotFoundError:
        print("")
    except ValueError:
        print("Value Error")
    except TypeError:
        print("Type Error")
    except Exception:
        print("Error inesperado")
        
        
        
        
print("c- cifrar \t d- descifrar  \t s-salir")
option = input()
while(option != "s"):
    if(option == "c"):
        print("Cifrar")
        cypher()
    if(option == "d"):
        print("Descifrar")
        decipher()
    if(option == "s"):
        break
    else: 
        print("c- cifrar \t d- descifrar  \t s-salir")
        option = input()
        
    
    

    