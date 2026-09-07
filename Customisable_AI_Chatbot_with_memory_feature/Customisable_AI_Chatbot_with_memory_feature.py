# Ai chatbot running locally with memory feature 
# Description= a chatbot running locally, built with llama3.2 and gradio. also has a feature to store conversation history
# You can also change LLM by your choice by downloading through Ollama for changing  see readme.md file  
# Created by Ojaswie Kumar Sanwariya 

import gradio as gr
from openai import OpenAI

client=OpenAI(base_url= "http://localhost:11434/v1", api_key="notneed")

def chat_with_llama(message, history):
    
    messages=[{"role": "system", "content": "you are a helpful assistant"}]
    
    for human, ai in history:
        messages.append({"role": "user", "content": human })
        messages.append({"role": "assistant", "content": ai })

    messages.append({"role": "user", "content": message})

    response=client.chat.completions.create(model="llama3.2",messages=messages,stream=True)

    result= ""

    for chunk in response:
        if chunk.choices[0].delta.content:
            result+=chunk.choices[0].delta.content
            yield result

gr.ChatInterface(chat_with_llama, title="AI Chatbot").launch()
