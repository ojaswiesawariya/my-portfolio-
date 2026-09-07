# AutoBrochure: AI Marketing Generator
# Description: A local AI pipeline that scrapes website text and automatically generates marketing brochures using Llama 3.2 and Gradio.
# To change the LLM via Ollama, refer to the README.md file for instructions.
# Created by Ojaswie Kumar Sanwariya

import gradio as gr
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key ="not-needed")

def generate_brochure(company_name,url):
    try:
        response= requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content,"html.parser")
        
        website_text= soup.get_text(separator="\n", strip=True)

        website_text = website_text[:4000]

    except Exception as e:
        yield f"Oops! Couldn't read the website. Error: {e}"
        return

    prompt= f"""You are an expert marketing copywriter. 
    I am going to give you the text scraped from the website of a company named {company_name}.
    
    Please write a professional, engaging 3-section brochure for them using Markdown format.
    Include:
    1. A catchy headline and "About Us" section.
    2. Key Services or Features.
    3. A strong Call to Action.
    
    Here is the website text:
    {website_text}
    """

    yield "Scraping complete! AI is now writing the brochure..."

    ai_response= client.chat.completions.create(model="llama3.2",
     messages= [{"role":"system", "content": "You are a helpful marketing assistant."}, {
        "role": "user", "content": prompt}],stream=True)

    result= ""
    for chunk in ai_response:
        if chunk.choices[0].delta.content:
            result+=chunk.choices[0].delta.content
            yield result

message_input=[
        gr.Textbox(label="Company Name", placeholder="e.g., Apple"),
        gr.Textbox(label="Website URL", placeholder="e.g., https://apple.com")]

message_outputs=[gr.Markdown(label="Generated Brochure")]      

view = gr.Interface(fn=generate_brochure,inputs=message_input, outputs =message_outputs,
 title="AI Brochure Generator",description="Enter a company name and website, and AI will write a marketing brochure for you!")

view.launch()