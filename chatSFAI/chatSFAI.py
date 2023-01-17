import openai
import time

# Apply your OpenAI API Key
openai.api_key = "<My API Key>"

#Base knowledge

opening = "Preste atenção no que eu vou te dizer, pois vou te contar o que eu sei sobre o assunto.\n" 
response = openai.Completion.create(engine="text-davinci-002", prompt=opening)
print(response["choices"][0]["text"])

data_file = "data.json"
informacao = open(data_file).read()
chunk_size = 7000
informacao_chunks = [informacao[i:i+chunk_size] for i in range(0, len(informacao), chunk_size)]

# Loop through each chunk and make an API call
i = 0
for chunk in informacao_chunks:
    i = i + 1
    response = openai.Completion.create(engine="text-davinci-002", prompt=chunk)
    time.sleep(1.5)
    print(f"Chunk: {i}/{len(informacao_chunks)}")

#Question
question = f"\nComo faço uma senha web?"
response = openai.Completion.create(engine="text-davinci-002", prompt=question)
print(response["choices"][0]["text"])
