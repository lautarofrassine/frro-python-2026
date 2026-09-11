def registrar_aplicacion_vacuna(mascota, vacuna, fecha_aplicacion):
    """Registra que una vacuna fue aplicada a una mascota en una
    fecha dada."""
    raise NotImplementedError


def calcular_proxima_dosis(mascota, vacuna):
    """Calcula la fecha de la próxima dosis sumando periodicidad_dias
    a la última aplicación."""
    raise NotImplementedError


def obtener_vacunas_proximas_a_vencer(dias=7):
    """Devuelve las próximas dosis de vacunación que vencen dentro de
    la cantidad de días indicada."""
    raise NotImplementedError
