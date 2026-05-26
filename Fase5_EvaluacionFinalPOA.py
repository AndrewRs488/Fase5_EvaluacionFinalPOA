# Datos iniciales de sesiones de clientes
# [ID Cliente, Duración (segundos), Eventos Clics]

sessions_data = [
    [101, 200, 10],
    [102, 45, 2],
    [103, 100, 5],
    [104, 300, 15],
    [105, 50, 7],
    [106, 185, 9],
    [107, 55, 1]
]

# Función para clasificar el compromiso
def classify_engagement(duration, clicks):

    if duration > 180 and clicks > 8:
        return "Alto"
    elif duration < 60 or clicks < 3:
        return "Bajo"
    else:
        return "Medio"

# Generar informe
print("Informe de Nivel de Compromiso de Sesiones:\n")

for session in sessions_data:

    client_id = session[0]
    duration = session[1]
    clicks = session[2]

    classification = classify_engagement(duration, clicks)

    print("ID Cliente:", client_id,
          "| Clasificación:", classification)