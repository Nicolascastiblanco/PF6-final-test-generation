import requests
import json

# ----------------------------------------------------
# Función que obtiene un plato según el número ingresado
# ----------------------------------------------------
def dish_fetch(num):
    url = "https://api-colombia.com/api/v1/TypicalDish"
    response = requests.get(url)
    dishes = response.json()

    # Validar que el número esté en rango
    if num < 0 or num >= len(dishes):
        return {"error": "Número fuera de rango"}

    return dishes[num]     # Retorna un diccionario con info del plato


# ----------------------------------------------------
# Función principal
# ----------------------------------------------------
def main():
    print("Hello learners!")

    # Pedir número al usuario
    num = int(input("Ingresa el número del plato que quieres ver: "))

    result = dish_fetch(num)

    print("\nResultado:")
    print(result)


# Ejecutar programa solo si es archivo principal
if __name__ == "__main__":
    main()



  