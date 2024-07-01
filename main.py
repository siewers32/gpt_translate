# from srt_to_vtt import srt_to_vtt

# path_to_my_srt_file = "input.srt"
# path_to_converted_vtt_file = "output.vtt"

# # converts example.srt into output.vtt
# srt_to_vtt(path_to_my_srt_file, path_to_converted_vtt_file)

from openai import OpenAI
client = OpenAI()



response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a sentence in English, and your task is to translate it into Dutch."
    },
    {
      "role": "user",
      "content": "My name is Jane. What is yours?"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)

print(response.choices[0].message)