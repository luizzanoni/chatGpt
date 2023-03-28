import openai
import gradio

openai.api_key = "##Sua api com a openai##"

# messages = [{"role": "system", "content": "Você é um assistente muito preguiçoso, que sempre responde de forma rude."}]
messages = [{"role": "system", "content": "Você é um assistente muito pró ativo, seja gentil"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Assistente Gentil")

demo.launch(share=False)