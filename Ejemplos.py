if 5>2:
   print ("Cinco es mayor que dos")
   Estatura:float=1.75
   print (Estatura)

   # Conversión de tipos de datos
   # Entero a decimal
   entero = 10
   decimal = float(entero)
   print(decimal)  # Salida: 10.0

   # Decimal a cadena
   decimal = 15.75
   cadena = str(decimal)
   print(cadena)  # Salida: '15.75'

   # Convertir entero a decimal
   entero_a_decimal = float(entero)
   print(entero_a_decimal)

   # Multilíneas de cadenas
   multilinea = """Esta es una cadena
   multilínea que abarca
   varias líneas."""
   print(multilinea)

   # Función len()
   cadena = "Hola, mundo soy Brayan"
   longitud = len(cadena)
   print(longitud)  # Salida: 22

   # Sub cadenas
   cadena = "Fundacion Universitaria de Popayan 2024"
   primeros = cadena[:9]
   en_medio = cadena[9:23]
   ultimos = cadena[-12:]

   print(primeros)  # Salida: 'Progr'
   print(en_medio)  # Salida: 'amación e'
   print(ultimos)  # Salida: 'Python'


   cadenaM = "Hola, Mundo  Upper"
   cadenam = "Hola, Mundo  Lower"
   # Función upper()
   print(cadenaM.upper())  # Salida: 'HOLA, MUNDO'
   # Función lower()
   print(cadenam.lower())  # Salida: 'hola, mundo'

   # Función strip()
   cadena_con_espacios = "   Hola, mundo!   "
   cadena_sin_espacios = cadena_con_espacios.strip()
   print(f"Cadena sin espacios: '{cadena_sin_espacios}'")

   # Función replace()
   cadena_reemplazada = cadena.replace("mundo", "Python")
   print(f"Cadena reemplazada: {cadena_reemplazada}")

   # Función split()
   cadena_separada = cadena.split(", ")
   print(f"Cadena separada: {cadena_separada}")

   # Formato de cadenas F-String
   nombre = "Brayan Hormiga"
   edad = 22
   cadena_formateada = f"Mi nombre es {nombre} y tengo {edad} años."
   print(cadena_formateada)
