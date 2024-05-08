import heapq

def heuristic(posicion_actual, objetivo):
    # Esta función heurística podría ser una estimación de la distancia entre la posición actual y el objetivo
    return abs(objetivo - posicion_actual)

def buscar_posicion_montaje_A_estrella(posicion_inicial_B, delta_H, objetivo):
    # Cola de prioridad para almacenar las posiciones a explorar, ordenadas por la suma de g(n) + h(n)
    cola_prioridad = []
    # Diccionario para almacenar los costos reales de llegar a cada posición
    costo_real = {}
    # Lista para almacenar los pasos tomados
    pasos = []
    
    # Definir límites para las posiciones exploradas
    lim_inf = 0
    lim_sup = 150
    
    # Agregar la posición inicial a la cola de prioridad con costo cero
    heapq.heappush(cola_prioridad, (0, posicion_inicial_B))
    costo_real[posicion_inicial_B] = 0
    
    # Mientras haya posiciones por explorar en la cola de prioridad
    while cola_prioridad:
        # Obtener la posición actual de la cola de prioridad
        costo, posicion_actual = heapq.heappop(cola_prioridad)
        
        # Verificar si la posición actual está dentro de los límites permitidos
        if lim_inf <= posicion_actual <= lim_sup:
            # Agregar el paso actual a la lista de pasos
            pasos.append(posicion_actual)
        
            # Verificar si la posición actual es el objetivo
            if posicion_actual == objetivo:
                print("Pasos tomados:")
                print(pasos)
                return costo  # Devolver el costo real de llegar al objetivo como resultado
        
            # Generar nuevas posiciones hacia la izquierda y derecha
            nueva_posicion_izquierda = posicion_actual - delta_H
            nueva_posicion_derecha = posicion_actual + delta_H
            
            # Calcular el nuevo costo real y estimado para cada nueva posición
            costo_izquierda = costo_real[posicion_actual] + 1  # Se asume que el costo de cada movimiento es 1
            costo_derecha = costo_real[posicion_actual] + 1
            estimado_izquierda = costo_izquierda + heuristic(nueva_posicion_izquierda, objetivo)
            estimado_derecha = costo_derecha + heuristic(nueva_posicion_derecha, objetivo)
            
            # Actualizar el costo real y agregar nuevas posiciones a la cola de prioridad si es necesario
            if nueva_posicion_izquierda not in costo_real or costo_izquierda < costo_real[nueva_posicion_izquierda]:
                costo_real[nueva_posicion_izquierda] = costo_izquierda
                heapq.heappush(cola_prioridad, (estimado_izquierda, nueva_posicion_izquierda))
            if nueva_posicion_derecha not in costo_real or costo_derecha < costo_real[nueva_posicion_derecha]:
                costo_real[nueva_posicion_derecha] = costo_derecha
                heapq.heappush(cola_prioridad, (estimado_derecha, nueva_posicion_derecha))
    
    # Si no se encuentra el objetivo, devolver None
    return None

# Ejemplo de uso
posicion_inicial_B = 100  # Posición inicial B
delta_H = 1  # Incremento ΔH
objetivo = 30  # Posición objetivo A
costo = buscar_posicion_montaje_A_estrella(posicion_inicial_B, delta_H, objetivo)
if costo is not None:
    print(f"El costo real de llegar al objetivo es: {costo}")
else:
    print("No se encontró una solución.")
