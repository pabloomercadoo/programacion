class Servicio:
    def __init__(self, id, orden_trabajo_id, descripcion, costo):
        self.id = id
        self.orden_trabajo_id = orden_trabajo_id
        self.descripcion = descripcion
        self.costo = costo
        self.validar_costo()

    def validar_costo(self):
        if self.costo < 0:
            raise ValueError(f"El costo no puede ser negativo. Valor recibido: {self.costo}")

    def __str__(self):
        return f"Servicio #{self.id} - OrdenTrabajo #{self.orden_trabajo_id}\n" \
               f"Descripción: {self.descripcion}\nCosto: ${self.costo:.2f}"