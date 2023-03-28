import openai

openai.api_key = "COLOCAR KEY OPENAI AQUI"

conversation = "Operador es un chatbot que responde de manera amigable"

while True:
    question = input("Tu: ")
    conversation += "\nTu: " + question + "\nOperador:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.5,
        max_tokens=100,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=[" Tu:"," Operador:"]
    )

    answer = response.choices[0].text.strip()
    conversation += answer
    print("Operador: " + answer + "\n")