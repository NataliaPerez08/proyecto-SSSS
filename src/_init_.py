"""
author = "Natalia Pérez Romero"
version = "1.0"
"""
import hashlib
import secrets

def horner_algorithm(x, n,coef):
    result = 0
    i=n-1
    while(i >= 0):
        result = (result * x) +coef[i]
        i = i-1
        
    return result
    
def generate_coefficients(re,k):
    coe = [h]
    for i in range(1,re):
        coe.append(secrets.randbelow(k)+1)
    return coe

def generate_evaluations(n,t,k,coef):
    evaluations = []
    for i in range(t):
        x = secrets.randbelow(k)+1
        tmp = horner_algorithm(x,n,coef)
        evaluations.append(tmp)
    return evaluations
        
    


def cypher():
    #file = str(input())   # Archivo para guarda n evaluaciones del polinomio
    #n = int(input())  # num total de evaluaciones requeridas n>2
    #t = int(input())   # num minimo de puntos necesarios para decifrar 1<t<n
    #clean_file = str(input()) # nombre del archivo con el documento claro
    print("Contraseña: ")
    password = str(input()).encode('utf-8')
    h = hashlib.sha256(password).hexdigest()
    k = int(h,16)
    #coefficients = generate_coefficients(t+1,k) # Grado del polinomio
    
    k=20
    prueba = [0,0,1]
    ev = generate_evaluations(3,2,k,prueba)
    
    for i in ev:
        print(i)
    
    

    
    
def decipher():
    evaluations_file = str(input()) # archivo con t de las n evaluaciones de polinomio
    encrypted_file = str(input()) # nombre del archivo cifrado
    
    
    
print("c- cifrar \t d- descifrar  \t s-salir")
option = input()
while(option != "s"):
    if(option == "c"):
        print("Cifrar")
        cypher()
    if(option == "d"):
        print("Descifrar")
        decipher
    if(option == "s"):
        break
    else: 
        print("c- cifrar \t d- descifrar  \t s-salir")
        option = input()
    
    

    