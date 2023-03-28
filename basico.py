import openai

openai.api_key = "##Sua api com a openai##"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                          messages=[{"role": "user", "content": "quanto é 2 + 2?"}])
print(completion.choices[0].message.content)