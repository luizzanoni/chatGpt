import openai

openai.api_key = "##Sua api com a openai##"

messages = []
# Descreva aqui como que você quer que ele seja. Rude, gentil, direto, amigável...
system_msg = input("Que tipo de chatbot você quer criar?\n")
messages.append({"role": "system", "content": system_msg})

print("Seu novo assistente está pronto!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
