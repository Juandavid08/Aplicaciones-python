characters = [
    {
        "name": "Albert Einstein",
        "questions": [
            "¿Es tu personaje famoso por su contribución a la física?",
            "¿Es tu personaje conocido por su teoría de la relatividad?",
        ]
    },
    {
        "name": "Leonardo da Vinci",
        "questions": [
            "¿Es tu personaje famoso por sus habilidades artísticas?",
            "¿Es tu personaje conocido por la pintura de la Mona Lisa?",
        ]
    },
    {
        "name": "Marie Curie",
        "questions": [
            "¿Es tu personaje famoso por sus contribuciones a la ciencia?",
            "¿Es tu personaje conocido por sus investigaciones sobre la radiactividad?",
        ]
    },
    {
        "name": "William Shakespeare",
        "questions": [
            "¿Es tu personaje famoso por su obra literaria?",
            "¿Es tu personaje conocido por sus obras como Romeo y Julieta o Hamlet?",
        ]
    },
    {
        "name": "Cristiano Ronaldo",
        "questions": [
            "¿Es tu personaje famoso por su carrera como futbolista?",
            "¿Es tu personaje conocido por haber jugado en el Real Madrid?",
        ]
    },
    {
        "name": "Lionel Messi",
        "questions": [
            "¿Es tu personaje famoso por su carrera como futbolista?",
            "¿Es tu personaje conocido por haber jugado en el FC Barcelona?",
        ]
    },
    {
        "name": "Gustavo Petro",
        "questions": [
            "¿Es tu personaje una figura política?",
            "¿Es tu personaje conocido por su participación en la política colombiana?",
        ]
    },
    {
        "name": "Napoleón Bonaparte",
        "questions": [
            "¿Es tu personaje una figura histórica?",
            "¿Es tu personaje conocido por ser un líder militar durante las guerras napoleónicas?",
        ]
    },
    {
        "name": "Simón Bolívar",
        "questions": [
            "¿Es tu personaje una figura histórica?",
            "¿Es tu personaje conocido por ser uno de los líderes en la lucha por la independencia de varios países de América del Sur?",
        ]
    },
    {
        "name": "Eminem",
        "questions": [
            "¿Es tu personaje un cantante de rap?",
            "¿Es tu personaje conocido por canciones como 'Lose Yourself' y 'Rap God'?",
        ]
    },
    {
        "name": "Jay-Z",
        "questions": [
            "¿Es tu personaje un cantante de rap?",
            "¿Es tu personaje conocido por su discografía y por ser uno de los artistas de hip-hop más influyentes?",

    ]
  },

];

def playGame():
    currentQuestionIndex = 0
    currentCharacterIndex = 0

    def showNextQuestion():
        nonlocal currentQuestionIndex
        nonlocal currentCharacterIndex

        if currentQuestionIndex >= len(characters[currentCharacterIndex]["questions"]):
            guessedCharacter = characters[currentCharacterIndex]["name"]
            print("Creo que estás pensando en: " + guessedCharacter)
        else:
            question = characters[currentCharacterIndex]["questions"][currentQuestionIndex]
            userResponse = input(question + " (Responde 'sí' o 'no'): ")
            userResponse = userResponse.lower()

            if userResponse == "sí" or userResponse == "si":
                currentQuestionIndex += 1
            elif userResponse == "no":
                currentCharacterIndex += 1
                currentQuestionIndex = 0
            else:
                print("Respuesta inválida. Por favor, responde 'sí' o 'no'.")

            showNextQuestion()

    showNextQuestion()

playGame()
