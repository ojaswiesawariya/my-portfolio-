**Customisable Local AI Chatbot with memory feature**

A local web interface for interacting with Large Language Models (LLMs), featuring conversational memory. Built using Gradio and Ollama.

**Prerequisites**
* Install [Ollama](https://ollama.com/).
* Pull the required model via terminal: `ollama run llama3.2`
* Ensure the Ollama server is running locally in the background.

**Installation**
1. Clone the repository.
2. Install the required dependencies:
   `pip install -r requirements.txt`

**Usage**
Run the script to launch the Gradio interface locally:
`python app.py`

How to Change the LLM

Open your terminal and download a new model using Ollama (e.g., ollama pull mistral).
Open Customisable_AI_Chabbot.py in your code editor.
Locate the ask_llama function on line 11.
Change the model="llama3.2" argument to match your downloaded model (e.g., model="mistral").