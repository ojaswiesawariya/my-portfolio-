# TEXT TO UPPERCASE CONVERTER 
# DESCRIPTION= A SIMPLE WEB INTERFACE BUILT WITH GRADIO THAT CONVERT USER INPUT TEXT TO UPPERCASE 
#CREATED BY OJASWIE KUMAR SANWARIYA  
import gradio as gr

def shout(text):
    return text.upper()

demo= gr.Interface(fn=shout, inputs="textbox", outputs="textbox")

demo.launch(share=True)