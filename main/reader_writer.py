"""
author = "Natalia Pérez Romero"
version = "1.0"
"""

# Lee el contenido en un archivo 
# Recibe el nombre del archivo
# Regresa el contenido de archivo o una cadena vacía
def read_txt(file_name):
    try:
        with open(file_name,'r') as f:
            text = f.read()
            return text
    except FileNotFoundError:
        print("No se encontro el archivo")
        return ""



    
# Escribe en un archivo el contenido
# Recibe el nombre del archivo donde escribir, y
# el contenido a escribir
# Regresa un booleano   
def write_txt(file_name,content):
    try:
        with open(file_name,'w') as f:
            f.write(content)
            return True
    except FileNotFoundError:
        print("No se encontro el archivo")
        return False

