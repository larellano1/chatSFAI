import openai
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Apply your OpenAI API Key
openai.api_key = "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"

#Base knowledge

opening = "Preste atenção no que eu vou te dizer, pois vou te contar o que eu sei sobre o assunto.\n" 
response = openai.Completion.create(engine="text-davinci-002", prompt=opening)
print(response["choices"][0]["text"])

data_file = "C:\\Users\\d805664\\Documents\\chatSFAI\\chatSFAI\\myproject\\myproject\\spiders\\data.json"
informacao = open(data_file).read()
chunk_size = 4000
informacao_chunks = [informacao[i:i+chunk_size] for i in range(0, len(informacao), chunk_size)]

# Loop through each chunk and make an API call
for chunk in informacao_chunks:
    response = openai.Completion.create(engine="text-davinci-002", prompt=chunk)
    print(response["choices"][0]["text"])

#Question
question = f"\nComo faço uma senha web?"
response = openai.Completion.create(engine="text-davinci-002", prompt=question)
print(response["choices"][0]["text"])
