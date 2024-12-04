"""
Repositorio en git listo
"""

#vamos a poner el 10 aqui igual

#ingresamos el nombre del archivo original
input_file = "preproinsulin-seq.txt"

#creamos donde vamos a guardar el archivo limpiado con el nombre
output_file = "preproinsulin-seq-clear.txt"

with open(input_file , 'r') as archivo:
    contenido = archivo.read()
        
# Eliminar 'ORIGIN', '//' y los números (como 1, 61)
clean_sequence = contenido.replace("ORIGIN", "") \
                          .replace("//", "") \
                          .replace("1", "") \
                          .replace("61", "") \
                          .replace("\n", "")  # Eliminar saltos de línea

# Eliminar los espacios
clean_sequence = clean_sequence.replace(" ", "").lower()

# Elimina posibles saltos de línea o espacios adicionales al principio y final
clean_sequence = clean_sequence.strip()

cantidad_char = len(clean_sequence)
print(cantidad_char)

with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.write(clean_sequence)
    
with open('preproinsulin-seq-clean.txt', 'r') as file:
    contenido = file.read()
    
print(len(contenido))

# Sub-secuencias
lsinsulin = clean_sequence[:24]    # Aminoácidos 1–24
binsulin = clean_sequence[24:54]  # Aminoácidos 25–54
cinsulin = clean_sequence[54:89]  # Aminoácidos 55–89
ainsulin = clean_sequence[89:110] # Aminoácidos 90–110

# Guardar en archivos
with open('lsinsulin-seq-clean.txt', 'w') as file:
    file.write(lsinsulin)

with open('binsulin-seq-clean.txt', 'w') as file:
    file.write(binsulin)

with open('cinsulin-seq-clean.txt', 'w') as file:
    file.write(cinsulin)

with open('ainsulin-seq-clean.txt', 'w') as file:
    file.write(ainsulin)

# Verificar las longitudes de los archivos
print(f"Longitud de lsinsulin: {len(lsinsulin)}")
print(f"Longitud de binsulin: {len(binsulin)}")
print(f"Longitud de cinsulin: {len(cinsulin)}")
print(f"Longitud de ainsulin: {len(ainsulin)}")
