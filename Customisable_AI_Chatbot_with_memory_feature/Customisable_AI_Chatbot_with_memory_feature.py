# AI CHATBOT RUNING LOCALLY WITH MEMORY FEATURE 
# DESCRIPTION= A CHATBOT RUNNING LOCALLY, BUILT WITH llama3.2 AND GRADIO. ALSO HAVE FEATURE TO STORE CONVERSATION HISTORY
#CREATED BY OJASWIE KUMAR SANWARIYA
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