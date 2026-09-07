# Ai Chatbot Running Locally With Memory Feature 
# Description= A Chatbot Running Locally, Built With Llama3.2 And Gradio. Also Have Feature To Store Conversation History
# You Can Also Change LLM By Your Choice By Downloading Through Ollama For Changing LLM See readme.md File  
# Created By Ojaswie Kumar Sanwariya 

import gradio as gr
from openai import OpenAI

client =OpenAI(base_url= "http://localhost:11434/v1", api_key="notneed")

def chat_with_llama(message,history):
    
    messages= [{"role": "system", "content": "you are a helpful assistant"}]
    
    for human, ai in history:
        messages.append({"role": "user", "content": human })
        messages.append({"role": "assistant", "content": ai })

    messages.append({"role": "user", "content": message})

    response= client.chat.completions.create(model="llama3.2",messages=messages,stream=True)

    result= ""

    for chunk in response:
        if chunk.choices[0].delta.content:
            result+=chunk.choices[0].delta.content
            yield result

gr.ChatInterface(chat_with_llama, title="AI Chatbot").launch()
