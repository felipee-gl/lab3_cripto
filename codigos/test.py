# Abre el archivo en modo lectura
with open('rockyou.txt', 'r', encoding="latin-1") as archivo:
    lineas = archivo.readlines()

# Paso 1 y 2
lineas_modificadas = []
for linea in lineas:
    linea = linea.strip()  # Elimina los espacios en blanco al principio y al final
    if len(linea) > 0:  # Verifica que la línea no esté vacía
        if not linea[0].isdigit():
            nueva_linea = linea.capitalize() + '0\n'
            lineas_modificadas.append(nueva_linea)

cantidad_strings_finales = len(lineas_modificadas)

with open('rockyou_mod.dic', 'w') as archivo_salida:
    archivo_salida.writelines(lineas_modificadas)

print(f"La cantidad de strings finales es: {cantidad_strings_finales}")