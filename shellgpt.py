import openai

# Configura tu clave API
openai.api_key = "tu_clave_API_aqui"

while True:
    pregunta = input("ShellGPT> ")
    if pregunta:
        try:
            # Llamar a la API de OpenAI
            respuesta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": pregunta}
                ],
                max_tokens=400
            )

            respuesta_texto = respuesta.choices[0].message['content'].strip()
            print(f'ShellGPT> {respuesta_texto}')
        except Exception as error:
            print(f'Error al obtener la respuesta de ShellGPT: {error}')
    else:
        print("Por favor, ingresa una pregunta.")
