def jugar_trivia(preguntas):
    aciertos = 0
    for pregunta in preguntas:
        correcta = pregunta["respuesta_correcta"]
        texto_correcto = pregunta["opciones"][correcta]

        mostrar_pregunta(pregunta)

        respuesta_usuario = obtener_respuesta()
        if verificar_respuesta(respuesta_usuario, correcta):
            aciertos += 1
            print(f"Bien Hecho, acertaste.\nTu puntaje Actual es: {aciertos}")
        else:
            print(f"Incorrecto, La respuesta correcta era: ({correcta}: {texto_correcto})")
    print(f"\n🎉 Trivia finalizada. Aciertos totales: {aciertos}/{len(preguntas)}")

def mostrar_pregunta(pregunta):
    print(f"La Pregunta es: {pregunta['pregunta']}")
    print()
    for opcion in pregunta.get("opciones").items():
        print(f"{opcion[0]}: {opcion[1]}")

def obtener_respuesta():
    while True:
        respuesta = input("Ingrese la letra de su respuesta:\n >>>").upper()
        if respuesta in ["A", "B", "C", "D"]:
            return respuesta
        else:
            print("Respuesta inválida. Ingrese A, B, C o D.")


def verificar_respuesta(respuesta_usuario, respuesta_correcta):
    return respuesta_usuario == respuesta_correcta


    
                    
preguntas = [
    {
    "pregunta": "¿Cuál es la capital de Francia?",
    "opciones": {"A": "Berlin", "B": "Santiago", "C": "Madrid", "D": "Paris"},
    "respuesta_correcta": "D"
    },
    {
    "pregunta": "¿Qué lenguaje se ejecuta en un navegador?",
    "opciones": {"A": "HTML", "B": "Python", "C": "React", "D": "C#"},
    "respuesta_correcta": "A"
    },
    {
    "pregunta": "¿Qué planeta es el más cercano al sol?",
    "opciones": {"A": "Tierra", "B": "Mercurio", "C": "Jupiter", "D": "Neptuno"},
    "respuesta_correcta": "B"
    }
]

jugar_trivia(preguntas)