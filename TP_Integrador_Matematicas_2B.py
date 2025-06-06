

from datetime import datetime



def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def ingresar_anios():
    anios = []
    for i in range(5):
        while True:  
            try:
                anio = int(input(f"Ingrese el año de nacimiento del integrante #{i + 1}: "))
                if (anio <= 0):
                    print("Error: El año debe ser positivo.")
                    continue
                anios.append(anio)
                break
            except ValueError:
                print("Error: Ingrese un año válido (ej: 1990).")
    
    return anios

def contar_pares_impares(aniosLista):
    pares = 0
    impares = 0
    
    for anio in aniosLista:
        if(anio %2 == 0):
            pares+=1
        else:
            impares+=1    

    return pares, impares

def edades_actuales(aniosLista):
    anio_actual = datetime.now().year

    edades_actuales_list = []

    for anioNacimiento in aniosLista:
        edad_actual_persona =  anio_actual - anioNacimiento
        edades_actuales_list.append(edad_actual_persona)

    return edades_actuales_list

def evaluar_condicione_grupoZ_o_bisiesto(anioslista):
    
    grupoZ = []
    bisiesto = []


    for anio in anioslista:
        if( anio > 2000):
           grupoZ.append(anio)
        elif(es_bisiesto(anio)):
            bisiesto.append(anio)
    
    return grupoZ, bisiesto  


def producto_cartesiano(aniosLista, edadesLista):
    resultado = []
    for anio in aniosLista:
        for edad in edadesLista:
            resultado.append((anio, edad))
    return resultado
   

def main():
    anios = ingresar_anios()
    
    pares, impares = contar_pares_impares(anios)
    print(f"\nCantidad de años pares: {pares}")
    print(f"Cantidad de años impares: {impares}")
    
    grupos = evaluar_condicione_grupoZ_o_bisiesto(anios)
    
    print("La cantidad de años del grupo Z (mayores a 2000) es ",str(len(grupos[0])),", estos son:", grupos[0])
    print("La cantidad de años bisiestos, un año especial es ",str(len(grupos[1])),", estos son:", grupos[1]) 


    edades = edades_actuales(anios)
    print("\nEdades actuales:")
    for i, edad in enumerate(edades):
        print(f"Integrante #{i + 1}: {edad} años")
    
    print("\nProducto cartesiano (Años x Edades):")
    productoCartesiano = producto_cartesiano(anios, edades)
    for producto in productoCartesiano:
        print(f"Año: {producto[0]}, Edad: {producto[1]}, Producto Cartesiano: {producto[0] , producto[1]}")

if __name__ == "__main__":
    main()