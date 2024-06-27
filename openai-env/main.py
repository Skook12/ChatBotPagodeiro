import openai

OPENAI_API_KEY="sk-proj-uQHsbRXxBVZ7H75IV391T3BlbkFJrAPxbHHUw6rKjtN1syBY"

openai.api_key = OPENAI_API_KEY
def enviar_mensagem(mensagem):
    completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um Pagodeiro, e responde a tudo com um pagode"},
        {"role": "user", "content": mensagem}
    ]
    )

    return(completion.choices[0].message)

while True:
    texto = input("Escreva a sua pergunta\n")
    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto)
        print(resposta.content+"\n")