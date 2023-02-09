import os
import openai

openai.api_key = "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"

prompt = "write a resume given the following text:\n"

prompt += "python, css, html, open-minded, NUS, responsible"

token_count = len(prompt.split())

response = openai.Completion.create(
        model="text-davinci-003",
        temperature=0.7,
        max_tokens=3900 - token_count,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

with open("test.txt", "w") as file:
    file.write(response.choices[0].text)
