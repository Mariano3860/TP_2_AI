def buscar_posicion_montaje_BFS(posicion_inicial_B, delta_H, objetivo):
    # Cola para almacenar las posiciones a explorar
    cola = []
    # Diccionario para almacenar las posiciones exploradas y su nivel en el árbol de búsqueda
    explorado = {}
    # Lista para almacenar los pasos tomados
    pasos = []
    # Limite inferior
    lim_inf = 0;
    # Limite superior
    lim_sup = 150;

    
    # Agregar la posición inicial a la cola y al diccionario de explorados
    cola.append((posicion_inicial_B, 0))
    explorado[posicion_inicial_B] = 0
    
    # Mientras haya posiciones por explorar en la cola
    while cola:
        # Obtener la posición actual y su nivel en el árbol de búsqueda
        posicion_actual, nivel_actual = cola.pop(0)
        
        # Agregar el paso actual a la lista de pasos
        pasos.append(posicion_actual)
        
        # Verificar si la posición actual es el objetivo
        if posicion_actual == objetivo:
            print("Pasos tomados:")
            print(pasos)
            return nivel_actual  # Devolver el nivel en el árbol de búsqueda como resultado
        
        # Generar nuevas posiciones hacia la izquierda y derecha y agregarlas a la cola
        nueva_posicion_izquierda = posicion_actual - delta_H
        nueva_posicion_derecha = posicion_actual + delta_H
        
        # Verificar si las nuevas posiciones están dentro del rango permitido y no han sido exploradas
        if lim_inf <= nueva_posicion_izquierda <= lim_sup and nueva_posicion_izquierda not in explorado:
            cola.append((nueva_posicion_izquierda, nivel_actual + 1))
            explorado[nueva_posicion_izquierda] = nivel_actual + 1
        if lim_inf <= nueva_posicion_derecha <= lim_sup and nueva_posicion_derecha not in explorado:
            cola.append((nueva_posicion_derecha, nivel_actual + 1))
            explorado[nueva_posicion_derecha] = nivel_actual + 1
    
    # Si no se encuentra el objetivo, devolver None
    return None

# Ejemplo de uso
posicion_inicial_B = 100  # Posición inicial B
delta_H = 1  # Incremento ΔH
objetivo = 30  # Posición objetivo A
nivel = buscar_posicion_montaje_BFS(posicion_inicial_B, delta_H, objetivo)
if nivel is not None:
    print(f"El nivel en el árbol de búsqueda para llegar al objetivo es: {nivel}")
else:
    print("No se encontró una solución.")
