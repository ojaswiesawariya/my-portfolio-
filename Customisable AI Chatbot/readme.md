**Customizable Local AI Chatbot**

A local web interface for interacting with Large Language Models (LLMs) using Gradio and Ollama.

**Prerequisites**
* Install [Ollama](https://ollama.com/).
* Pull your default model via terminal: `ollama run llama3.2`
* Ensure the Ollama server is running locally in the background.

**Installation**
1. Clone the repository.
2. Install the required Python packages:
   `pip install -r requirements.txt`

**Usage**
Run the script to launch the Gradio interface:
`python Customisable_AI_Chabbot.py`

**How to Change the LLM**
1. Open your terminal and download a new model using Ollama (e.g., `ollama pull mistral`).
2. Open `Customisable_AI_Chabbot.py` in your code editor.
3. Locate the `ask_llama` function on line 11.
4. Change the `model="llama3.2"` argument to match your downloaded model (e.g., `model="mistral"`).