# AutoBrochure: AI Marketing Generator

A local AI tool that scrapes a company's website and automatically generates a professional, 3-section marketing brochure. Built with Python, BeautifulSoup, Gradio, and Llama 3.2 via Ollama.

## Features
* **Web Scraping:** Automatically extracts readable text from any provided URL.
* **Local AI Processing:** Uses a local LLM to guarantee privacy and avoid API costs.
* **Real-time Streaming:** Generates the brochure dynamically in the UI.

## Prerequisites
* Install [Ollama](https://ollama.com/).
* Pull the default model via terminal: `ollama run llama3.2`
* Ensure the Ollama server is running locally in the background.

## Installation
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

**usage**

Run the script to launch the Gradio interface locally: python AI_Marketing_Generator.py

**How to Change the LLM**

Open your terminal and download a new model using Ollama (e.g., ollama pull mistral).
Open AI_Marketing_Generator.py in your code editor.
Locate the client.chat.completions.create function call.
Change the model="llama3.2" argument to match your downloaded model (e.g., model="mistral").