# AI Chatbot running locally
# DESCRIPTION=this Chatbot running locally in system built with Llama3.2 and gradio
# You can also change LLM by your choice by downloading through Ollama for changing LLM see readme.md file  
#CREATED BY OJASWIE KUMAR SANWARIYA 
import gradio as gr
from openai import OpenAI

client = OpenAI(base_url= "http://localhost:11434/v1", api_key="notneed")

def ask_llama(prompt):
    response = client.chat.completions.create(model="llama3.2", messages=[{"role": "system", "content": "you are a helpful assistant"},
    {"role": "user", "content": prompt}],stream=True) 

    result = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            result+=chunk.choices[0].delta.content
            yield result

view = gr.Interface(fn=ask_llama, title = "Ai chatbot",inputs=gr.Textbox(label="Talk to your chatbot",info= "How can I help you",lines=5),
outputs =gr.Markdown(label="chatbot Response"),examples= ["Who invented the lightbulb?"],)
view.launch()