# Text To Uppercase Converter 
# Description= A Simple Web Interface Built With Gradio That Convert User Input Text To Uppercase 
#Created By Ojaswie Kumar Sanwariya  
import gradio as gr

def shout(text):
    return text.upper()

demo= gr.Interface(fn=shout, inputs="textbox", outputs="textbox")

demo.launch()
