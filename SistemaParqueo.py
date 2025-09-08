2
# Sistema de Parqueo Simple 

import random

# CONSTANTES
CAPACIDAD_MAXIMA = 50
TARIFA_POR_HORA = 3.0

# VARIABLES
espacios_ocupados = 0
autos_estacionados = []
eventos = []

print("=== SISTEMA DE PARQUEO SIMPLE ===")
print(f"Capacidad máxima: {CAPACIDAD_MAXIMA} espacios")
print(f"Tarifa por hora: ${TARIFA_POR_HORA}")
print()


def generar_placa():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    placa = ""
    for i in range(4):
        placa = placa + random.choice(letras)
    for i in range(4):
        placa = placa + str(random.randint(0, 9))
    return placa

# Función para calcular porcentaje de ocupación
def calcular_porcentaje():
    porcentaje = (espacios_ocupados * 100) / CAPACIDAD_MAXIMA
    return porcentaje

# Función de estado del parqueo
def obtener_estado():
    porcentaje = calcular_porcentaje()
    if porcentaje >= 90:
        return "LLENO"
    elif porcentaje >= 50:
        return "MEDIO OCUPADO"
    else:
        return "DISPONIBLE"

# Función para mostrar información del parqueo
def mostrar_info():
    espacios_libres = CAPACIDAD_MAXIMA - espacios_ocupados
    porcentaje = calcular_porcentaje()
    estado = obtener_estado()
    
    print("\n--- ESTADO DEL PARQUEO ---")
    print(f"Espacios ocupados: {espacios_ocupados}")
    print(f"Espacios libres: {espacios_libres}")
    print(f"Porcentaje ocupado: {porcentaje:.1f}%")
    print(f"Estado: {estado}")
    print()

# Función para que entre un auto
def auto_entra():
    global espacios_ocupados
    
    # Verificar si hay espacio
    if espacios_ocupados >= CAPACIDAD_MAXIMA:
        print("ERROR: El parqueo está lleno!")
        return False
    
    # Generar placa y agregar auto
    placa = generar_placa()
    espacios_ocupados = espacios_ocupados + 1
    autos_estacionados.append(placa)
    
    # Guardar evento (placa, tipo, tarifa)
    evento = (placa, "ENTRADA", 0.0)
    eventos.append(evento)
    
    print(f"Auto {placa} ENTRÓ al parqueo")
    return True

# Función para que salga un auto
def auto_sale():
    global espacios_ocupados
    
    # Verificar si hay autos
    if espacios_ocupados <= 0:
        print("ERROR: No hay autos en el parqueo!")
        return False
    
    # Elegir un auto al azar para que salga
    placa = random.choice(autos_estacionados)
    espacios_ocupados = espacios_ocupados - 1
    autos_estacionados.remove(placa)
    
    # Calcular tarifa
    horas = random.randint(1, 6)
    tarifa = horas * TARIFA_POR_HORA
    
    evento = (placa, "SALIDA", tarifa)
    eventos.append(evento)
    
    print(f"Auto {placa} SALIÓ del parqueo - Pagó: ${tarifa:.2f}")
    return True

# Función para mostrar todos los autos estacionados
def mostrar_autos():
    print("\n--- AUTOS ESTACIONADOS ---")
    if len(autos_estacionados) == 0:
        print("No hay autos estacionados")
    else:
        for i in range(len(autos_estacionados)):
            print(f"{i+1}. {autos_estacionados[i]}")
    print(f"Total: {len(autos_estacionados)} autos")
    print()

# Función para mostrar historial de eventos
def mostrar_historial():
    print("\n--- HISTORIAL DE EVENTOS ---")
    if len(eventos) == 0:
        print("No hay eventos registrados")
    else:
        for i in range(len(eventos)):
            placa, tipo, tarifa = eventos[i]
            if tipo == "ENTRADA":
                print(f"{i+1}. {placa} - {tipo}")
            else:
                print(f"{i+1}. {placa} - {tipo} - ${tarifa:.2f}")
    print()

print("Agregando algunos autos iniciales...")
for i in range(10):
    auto_entra()

mostrar_info()


while True:
    print("\n=== MENÚ ===")
    print("1. Ver estado del parqueo")
    print("2. Entran autos (aleatorio)")
    print("3. Salen autos (aleatorio)")
    print("4. Ver autos estacionados")
    print("5. Ver historial")
    print("6. Simular movimiento")
    print("0. Salir")
    
    try:
        opcion = input("\nElige una opción (0-6): ")
        
        if opcion == "1":
            mostrar_info()
            
        elif opcion == "2":
            try:
                cantidad = input("¿Cuántos autos entran? (Enter para aleatorio): ")
                if cantidad == "":
                    cantidad = random.randint(1, 5)
                else:
                    cantidad = int(cantidad)
                
                if cantidad < 0:
                    print("ERROR: No puedes usar números negativos")
                elif cantidad == 0:
                    print("No entran autos")
                else:
                    print(f"\nEntrando {cantidad} autos...")
                    for i in range(cantidad):
                        if not auto_entra():
                            break
                    mostrar_info()
                
            except:
                print("ERROR: Debes escribir un número")
                
        elif opcion == "3":
            try:
                cantidad = input("¿Cuántos autos salen? (Enter para aleatorio): ")
                if cantidad == "":
                    cantidad = random.randint(1, 3)
                else:
                    cantidad = int(cantidad)
                
                if cantidad < 0:
                    print("ERROR: No puedes usar números negativos")
                elif cantidad == 0:
                    print("No salen autos")
                else:
                    print(f"\nSaliendo {cantidad} autos...")
                    for i in range(cantidad):
                        if not auto_sale():
                            break
                    mostrar_info()
                
            except:
                print("ERROR: Debes escribir un número")
                
        elif opcion == "4":
            mostrar_autos()
            
        elif opcion == "5":
            mostrar_historial()
            
        elif opcion == "6":
            print("\nSimulando movimiento aleatorio...")
            entran = random.randint(1, 4)
            print(f"Entran {entran} autos:")
            for i in range(entran):
                if not auto_entra():
                    break
            
            salen = random.randint(1, 3)
            print(f"\nSalen {salen} autos:")
            for i in range(salen):
                if not auto_sale():
                    break
            
            mostrar_info()
            
        elif opcion == "0":
            print("\n¡Gracias por usar el sistema!")
            break
            
        else:
            print("ERROR: Opción no válida")
            
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego!")
        break
    except:
        print("ERROR: Entrada inválida")