#Nombre:
#Matricula:
#Grupo:
#Fecha:
import random

# Datos para generar nombres y ubicaciones
nombres = ["Miguel", "Ana", "Carlos", "Lucía", "Pedro", "Laura", "Juan", "Elena", "Mario", "Sofia"]
ubicaciones = ["Orizaba", "Nogales", "Mendoza", "Orizaba", "Mendoza", "Ixtac", "Orizaba", "Cordoba", "Cordoba", "Nogales"]
intereses = ["deporte", "cine", "música", "viajes", "lectura", "tecnología", "fotografía", "cocina", "arte", "naturaleza"]

# Crear personas con información aleatoria
class Persona:
    def __init__(self, nombre, ubicacion, intereses):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.intereses = intereses

    def __repr__(self):
        return f"Nombre: {self.nombre}, Ubicación: {self.ubicacion}, Intereses: {', '.join(self.intereses)}"

# Seleccionar 10 personas con intereses aleatorios de los datos definidos inicialmente
personas = []
for i in range(10):
    nombre = random.choice(nombres)
    ubicacion = random.choice(ubicaciones)
    intereses_persona = random.sample(intereses, 3)  # Seleccionamos 3 intereses aleatorios por persona
    personas.append(Persona(nombre, ubicacion, intereses_persona))

# Función de filtrado colaborativo: busca personas con al menos un interés común
def filtrar_colaborativo(persona, personas):
    coincidencias = []
    for otra_persona in personas:
        if persona != otra_persona:
            intereses_comunes = set(persona.intereses) & set(otra_persona.intereses)
            if intereses_comunes:
                coincidencias.append((otra_persona, intereses_comunes))
    return coincidencias

# Mostrar todas las personas
print("Lista de personas generadas:")
for persona in personas:
    print(persona)

# Seleccionamos una persona para hacer el filtrado colaborativo
persona_a_filtrar = random.choice(personas)
print(f"\nFiltrado colaborativo para: {persona_a_filtrar.nombre}")

# Aplicamos el filtrado colaborativo
coincidencias = filtrar_colaborativo(persona_a_filtrar, personas)

# Mostrar las coincidencias
if coincidencias:
    print("\nPersonas con intereses comunes:")
    for coincidencia, intereses_comunes in coincidencias:
        print(f"{coincidencia.nombre} - Intereses comunes: {', '.join(intereses_comunes)}")
else:
    print("No se encontraron coincidencias con intereses comunes.")
