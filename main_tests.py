"""
author = "Natalia Pérez Romero"
version = "1.0"
"""
import unittest
import random
from main import *
class Test(unittest.TestCase):

    # Prueba que lo que regresa el método de lectura sea lo esperado
    def test_reader(self): 
        read = read_txt("test.txt")
        ex = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        self.assertEqual(read,ex)
        
        
    # Prueba que lo que regresa el método de lectura sea lo esperado
    def test_reader_diff(self):
        read = read_txt("test.txt")
        ex = "Lorem ipsum dolor sit amet, consectetur adipiscing elit "
        self.assertNotEqual(read,ex)
        
    
    # Comprueba que lo que se escribe un método es lo mismo que va leer el otro método.
    def test_read_write(self):
        content="Advanced Encryption Standard (AES) es uno de los algoritmos de cifrado más utilizados y seguros actualmente disponibles. "
        write_txt("test2.txt",content)
        read = read_txt("test2.txt")
        self.assertEqual(content,read)
        
        
    # Prueba que se generen los coeficientes necesarios
    def test_generate_coefficients(self):
        i=random.randint(5,1000)
        while(i !=0):
            lge = generate_coefficients(i,1) # El num de coeficientes es igual al grado del polinomio
            l = len(lge)
            self.assertEqual(i,l)
            i=i-1
            
            
    # Prueba que el algorimo este correctamente implementado
    def test_horner_algorithm(self):
        coe = [1,0,1] # Es x^2+1
        x=random.randint(5,1000)
        while(x !=0):
            fx = horner_algorithm(x,3,coe)
            l = (x*x)+1
            self.assertEqual(l,fx)
            x=x-1
            
            
    # Prueba que dado dos puntos cuando se evalue 
    # el polinomio f(x)=Ax^2+k en f(0)=k en este caso 0
    def test_lagrande_polynomial(self):
        nlist = [[2,4],[4,8]]  # Dos puntos (x,fx) de x^2
        fx = lagrange_polynomial(nlist)
        self.assertEqual(0,fx)
    
    
    # Prueba que dado tres puntos cuando se evalue 
    # el polinomio f(x)=Ax^3+k en f(0)=k en este caso 5
    def test_lagrande_polynomial_2(self):
        nlist = [[0,5],[2,13]]  # Dos puntos (x,fx) de x^2
        fx = lagrange_polynomial(nlist)
        self.assertEqual(5,fx)
       

if __name__== '__main__':
    unittest.main()