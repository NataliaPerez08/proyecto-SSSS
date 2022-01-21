"""
author = "Natalia Pérez Romero"
version = "1.0"
"""
import hashlib
import secrets

from Crypto.Cipher import AES
from getpass import getpass

from reader_writer import read_txt,write_txt

def horner_algorithm(x, n,coef):
    result = 0
    i=n-1
    while(i >= 0):
        result = (result * x) +coef[i]
        i = i-1
    return result
    
def generate_coefficients(re,k):
    coe = [k]
    for i in range(1,re):
        coe.append(secrets.randbelow(k)+1)
    return coe

def generate_evaluations(n,t,k,coef):
    evaluations = []
    for i in range(t):
        x = secrets.randbelow(k)+1
        value = horner_algorithm(x,n,coef)
        tmp = str(x)+","+str(value)
        evaluations.append(tmp)
    return evaluations
        
    


def cypher():
    file = str(input())   # Archivo para guarda n evaluaciones del polinomio
    n = int(input())  # num total de evaluaciones requeridas n>2
    t = int(input())   # num minimo de puntos necesarios para decifrar 1<t<n
    clean_file = str(input()) # nombre del archivo con el documento claro
    
    print("Contraseña: ")
    password = str(getpass()).encode('utf-8').strip()
    h = hashlib.sha256(password).hexdigest()
    k = int(h,16)
    
    key = hashlib.sha256(password).digest()
    coefficients = generate_coefficients(t+1,k) # Grado del polinomio
    
    ev = generate_evaluations(n,t,k,coefficients) # lista
    
    texto = read_txt(clean_file)
    data = texto.encode("utf-8")
    cipher = AES.new(key,AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext,tag = cipher.encrypt_and_digest(data)
    
    ciphertext = ciphertext.hex()
    write_txt(clean_file+".aes",str(ciphertext))
    str_ev = "\n".join(str(i) for i in ev)
    write_txt(file+".frg",str_ev)
    

    
    
def decipher():
    evaluations_file = str(input()) # archivo con t de las n evaluaciones de polinomio
    #encrypted_file = str(input()) # nombre del archivo cifrado
    
    evfile = read_txt(evaluations_file)
    print(evfile)
    #cipher = AES.new(key, AES.MODE_EAX)
    #nonce = cipher.nonce
    #texto_plano = cipher.decrypt(ciphertext)
    #print(texto_plano.decode('utf-8'))
    
    
    
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
        
    
    

    