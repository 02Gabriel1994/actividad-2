#heapq permite trabajar con montículos o colas con prioridad
import heapq
class TransporteMasivo:
    def __init__(self):
        # Grafo para representar el sistema de transporte
        self.grafo = {}
    def agregar_estacion(self, estacion):
        # Agregamos una estación si no existe en el grafo
        if estacion not in self.grafo:
            self.grafo[estacion] = []
    def agregar_ruta(self, estacion_origen, estacion_destino, tiempo):
        # Agregamos una ruta (arista) entre dos estaciones con un peso asociado (tiempo)
        self.agregar_estacion(estacion_origen)
        self.agregar_estacion(estacion_destino)
        self.grafo[estacion_origen].append((estacion_destino, tiempo))
        self.grafo[estacion_destino].append((estacion_origen, tiempo))
# Regla lógica: condición para una ruta válida (pueden ser muchas más)
def regla_ruta_valida(self, origen, destino):
  # Definimos condiciones para que una ruta sea válida
        # Por ejemplo, evitar ciertas estaciones por mantenimiento o alta congestión
        return origen in self.grafo and destino in self.grafo
# Algoritmo de búsqueda de Dijkstra
# Sirve para encontrar el camino de coste mínimo desde un nodo origen a todos los demás nodos del grafo
def mejor_ruta(self, inicio, fin):
        # Comprobamos si hay una regla que impida el viaje
        if not self.regla_ruta_valida(inicio, fin):
            return None

        # Cola de prioridad para el algoritmo de Dijkstra
        cola_prioridad = [(0, inicio)]
        distancias = {inicio: 0}
        camino_previo = {inicio: None}

        while cola_prioridad:
            (dist_actual, estacion_actual) = heapq.heappop(cola_prioridad)

            if estacion_actual == fin:
                # Si hemos llegado a la estación destino, reconstruimos la ruta
                ruta = []
                while estacion_actual:
                    ruta.append(estacion_actual)
                    estacion_actual = camino_previo[estacion_actual]
                return ruta[::-1], dist_actual  # Devolvemos la ruta en orden y el tiempo total

            # Verificar rutas adyacentes
            for (vecino, tiempo) in self.grafo[estacion_actual]:
                dist = dist_actual + tiempo
                if vecino not in distancias or dist < distancias[vecino]:
                    distancias[vecino] = dist
                    camino_previo[vecino] = estacion_actual
                    heapq.heappush(cola_prioridad, (dist, vecino))

        return None  # Si no hay una ruta posible

        # Ejemplo de uso
        sistema_transporte = TransporteMasivo()

        # Definir el sistema de transporte (estaciones y rutas)
        sistema_transporte.agregar_ruta('A', 'B', 10)
        sistema_transporte.agregar_ruta('B', 'C', 15)
        sistema_transporte.agregar_ruta('A', 'D', 20)
        sistema_transporte.agregar_ruta('D', 'C', 5)
        sistema_transporte.agregar_ruta('C', 'E', 10)

        # Buscar la mejor ruta entre 'A' y 'E'
        ruta, tiempo_total = sistema_transporte.mejor_ruta('A', 'E')

        if ruta:
            print(f"La mejor ruta de A a E es: {' -> '.join(ruta)} con un tiempo total de {tiempo_total} unidades.")
        else:
            print("No hay una ruta válida entre A y E.")