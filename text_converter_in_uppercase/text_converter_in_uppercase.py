# Text to uppercase converter 
# Description= a simple web interface built with gradio that convert user input text to uppercase 
# Created by Ojaswie Kumar Sanwariya  
import gradio as gr

def shout(text):
    return text.upper()

demo= gr.Interface(fn=shout, inputs="textbox", outputs="textbox")

demo.launch()
