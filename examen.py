def manejar_caso(caso, a, b):
    resultado = {
        'caso1': a + b,  # P1
        'caso2': a * b,  # P2
    }.get(caso, "Caso predeterminado: operación no definida")  # P3
    
    return resultado

def main():
    lista_casos = ['caso1', 'caso2', 'caso3']  # P4
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))

    for caso in lista_casos:#P5
        resultado = manejar_caso(caso, a, b)
        print(f"Caso: {caso}, Resultado: {resultado}")

    return "Ejecución completa"  # P6

if __name__ == "__main__":
    mensaje_final = main()
    print(mensaje_final)