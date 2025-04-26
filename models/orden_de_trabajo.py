from datetime import datetime

class OrdenDeTrabajo:
    ESTADOS_VALIDOS = {"pendiente", "en progreso", "finalizado"}

    def __init__(self, id, vehiculo_id, fecha_ingreso, estado="pendiente", fecha_salida=None):
        self.id = id
        self.vehiculo_id = vehiculo_id
        self.fecha_ingreso = fecha_ingreso  
        self.fecha_salida = fecha_salida    
        self.estado = estado.lower()
        self.validar_estado()

    def validar_estado(self):
        if self.estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido: '{self.estado}'. Debe ser uno de {self.ESTADOS_VALIDOS}")

    def finalizar_orden(self):
        self.estado = "finalizado"
        self.fecha_salida = datetime.now()

    def __str__(self):
        salida = self.fecha_salida.strftime("%Y-%m-%d %H:%M") if self.fecha_salida else "Aún en taller"
        return f"Orden #{self.id} - Vehículo ID: {self.vehiculo_id}\n" \
               f"Ingreso: {self.fecha_ingreso.strftime('%Y-%m-%d %H:%M')}\n" \
               f"Salida: {salida}\nEstado: {self.estado.capitalize()}"