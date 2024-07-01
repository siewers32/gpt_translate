import tiktoken
from openai import OpenAI
client = OpenAI()

# enc = tiktoken.get_encoding("cl100k_base")
# # assert enc.decode(enc.encode("hello world")) == "hello world"

# # To get the tokeniser corresponding to a specific model in the OpenAI API:
# enc = tiktoken.encoding_for_model("gpt-4")

f = open("test.srt", "r")
txt = f.read()
w = open("output3.srt", "w")

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def translate(en_txt, out_file):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "system",
        "content": "You will be provided with a text in English, and your task is to translate it into Dutch."
        },
        {
        "role": "user",
        "content": en_txt
        }
    ],
    temperature=0.7,
    max_tokens=4000,
    top_p=1
    )
    out_file.write(response.choices[0].message.content)
    print(response.choices[0].message.content)

translate(txt, w)
f.close()
w.close()