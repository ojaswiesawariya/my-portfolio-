# AI CHATBOT RUNNING LOCALLY WITH MEMORY FEATURE AND MULIT MODEL SELECTION
# DESCRIPTION= A CHATBOT RUNING LOCALLY, BUILT WITH llama3.2, deepseek-r1:1.5b AND GRADIO. ALSO HAVE FEATURE TO STORE CONVERSATION HISTORY AND IT HAS 2 MODEL YOU CAN SELECT ANY
#CREATED BY OJASWIE KUMAR SANWARIYA

import gradio as gr
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key= "not-needed" )
def chat_with_multiple_model(message, history, model_choice):
    messages= [{"role": "system", "content": "you are a helpful assistant"}]

    for human, ai in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role":"assistant","content": ai})

    messages.append({"role": "user", "content": message})

    response= client.chat.completions.create(model=model_choice,messages=messages,stream=True)
    
    result= ""

    for chunk in response:
        if chunk.choices[0].delta.content:
            result+= chunk.choices[0].delta.content
            yield result

model_dropdown= gr.Dropdown(choices=["llama3.2", "deepseek-r1:1.5b"],value="llama3.2", label= "choice you'r AI brain")

gr.ChatInterface(fn=chat_with_multiple_model,additional_inputs=[model_dropdown],additional_inputs_accordion=gr.Accordion(label=" Select Model", open=False),
title= "  AI Multi chatbot" ).launch()