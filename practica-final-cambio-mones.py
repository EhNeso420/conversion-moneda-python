# Paso 1: Definir el valor actual del Euro y Dólar con respecto al Peso Mexicano

tipo_cambio_eur_a_mxn = 23.70 # En un caso real lo que se suele hacer es extraer este dato de una BDD o API
tipo_cambio_usd_a_mxn = 20.75 # En un caso real lo que se suele hacer es extraer este dato de una BDD o API

# Paso 2: Solicitar al usuario el tipo de conversión (Euro a Mex o Dólar a Mex)

tipo_de_conversion = input("Ingrese la moneda origen para la conversión (EUR/USD): ").upper()

# Paso 3: Solicitar al usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversión utilizando el tipo de cambio correspondiente
# Paso 5: Mostrar el resultado de la conversión al usuario

if tipo_de_conversion == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversión de EUR a MXN es: ", resultado)
elif tipo_de_conversion == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversión de USD a MXN es: ", resultado)
else:
    print("No está disponible este tipo de conversión actualmente")
