"""
author = "Natalia Pérez Romero"
version = "1.0"
"""
import hashlib
def cypher():
    #file = str(input())   # Archivo para guarda n evaluaciones del polinomio
    #required_evaluations = int(input())  # num total de evaluaciones requeridas n>2
    #min_point = int(input())   # num minimo de puntos necesarios para decifrar 1<t<n
    #clean_file = str(input()) # nombre del archivo con el documento claro
    password = str(input()).encode('utf-8')
    print(password)
    h = hashlib.sha256(password)
    print(h.hexdigest())
    
    
    
    
def decipher():
    evaluations_file = str(input()) # archivo con t de las n evaluaciones de polinomio
    encrypted_file = str(input()) # nombre del archivo cifrado
    
    
    
    
option = input()
while(option != "s"):
    print("c- cifrar \t d- descifrar  \t s-salir")
    if(option == "c"):
        print("Cifrar")
        cypher()
    if(option == "d"):
        print("Descifrar")
        decipher
    if(option == "s"):
        break
    else: option = input()
    
    

    