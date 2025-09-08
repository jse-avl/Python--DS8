# Sistema de Parqueo

Se desea implementar un sistema de parqueo inteligente para monitorear la ocupación de los 
estacionamientos en un centro comercial. El equipo debe simular en Python cómo funcionaría el 
sistema. Se deben generar datos simulados y procesarlos con Python.


## Cómo usar el programa

Cuando ejecutes el programa verás un menú con estas opciones:

### Explicación de cada opción:

- **Opción 1**: Muestra el estado actual del parqueo (ocupación, tarifa, estado)
- **Opción 2**: Permite que entren autos al parqueo (manual o aleatorio)
- **Opción 3**: Permite que salgan autos del parqueo (manual o aleatorio)
- **Opción 4**: Lista todas las placas de los autos estacionados
- **Opción 5**: Muestra el historial completo de entradas y salidas
- **Opción 6**: Simula movimiento automático de autos
- **Opción 0**: Cierra el programa


### Conceptos básicos de Python:
- **Variables globales**: `espacios_ocupados`, `autos_estacionados`, `eventos`
- **Constantes**: `CAPACIDAD_MAXIMA`, `TARIFA_POR_HORA`
- **Listas**: Para guardar placas y eventos
- **Tuplas**: Para almacenar eventos (placa, tipo, tarifa)
- **Funciones**: Para organizar el código
- **Bucles**: `for` y `while` para repetir acciones
- **Condicionales**: `if`, `elif`, `else` para tomar decisiones
- **Manejo de errores**: `try/except` para evitar que el programa se rompa
- **Entrada del usuario**: `input()` para interactuar
- **Números aleatorios**: `random` para simular datos

### Conceptos del sistema:
- **Constantes**: Valores que no cambian (capacidad: 50, tarifa: $3.00)
- **Variables**: Valores que cambian (espacios ocupados)
- **Estados**: DISPONIBLE, MEDIO OCUPADO, LLENO
- **Eventos**: Registro de entradas y salidas con tuplas
- **Validaciones**: Verificar espacios disponibles y errores

##  Características del sistema

- **Capacidad máxima**: 50 espacios
- **Tarifa**: $3.00 por hora
- **Placas automáticas**: Formato ABCD1234 (4 letras + 4 números)
- **Cálculo de ocupación**: Porcentaje en tiempo real
- **Estados del parqueo**: Según porcentaje de ocupación
- **Historial completo**: Todas las entradas y salidas
- **Manejo de errores**: Para entradas inválidas
- **Simulación**: Movimiento aleatorio de autos
- **Datos iniciales**: 10 autos agregados al inicio

## Cómo funciona el sistema

1. **Al iniciar**: El programa agrega 10 autos automáticamente
2. **Placas**: Se generan automáticamente (ej: ABCD1234)
3. **Entrada**: Se verifica que haya espacio disponible
4. **Salida**: Se calcula la tarifa según horas aleatorias (1-6 horas)
5. **Estados**:
   - **DISPONIBLE**: Menos del 50% ocupado
   - **MEDIO OCUPADO**: Entre 50% y 90% ocupado
   - **LLENO**: 90% o más ocupado

## Ejemplos de uso

### Ejemplo 1: Ver estado inicial
1. Ejecuta el programa
2. Elige la opción 1 (Ver estado del parqueo)
3. Observa que hay 10 autos estacionados y 40 espacios libres

### Ejemplo 2: Entrar 3 autos
1. Elige la opción 2 (Entran autos)
2. Cuando se te pregunte, escribe 3
3. Observa las placas generadas y el estado actual

### Ejemplo 3: Salir 2 autos
1. Elige la opción 3 (Salen autos)
2. Cuando se te pregunte, escribe 2
3. Observa las placas que salieron y el estado actual

### Ejemplo 4: Ver historial
1. Elige la opción 5 (Ver historial)
2. Observa todas las entradas y salidas con sus respectivas horas y tarifas
3. Nota: El historial incluye entradas y salidas de todos los autos, no solo los recientes