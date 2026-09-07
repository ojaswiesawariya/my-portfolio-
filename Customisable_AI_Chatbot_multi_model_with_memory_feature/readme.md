# Multi-Model Local AI Chatbot

A local web interface featuring conversational memory and the ability to seamlessly switch between multiple Large Language Models (LLMs). Built with Gradio and Ollama.

## Prerequisites
* Install [Ollama](https://ollama.com/).
* Pull the required models via terminal:
  * `ollama run llama3.2`
  * `ollama run deepseek-r1:1.5b`
* Ensure the Ollama server is running locally in the background.

## Installation
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

   **Usage** 
   Run the script to launch the Gradio interface locally: python Customisable_AI_Chatbot_multi_model_with_memory_feature.py

**How to Change the LLM**

Open your terminal and download a new model using Ollama (e.g., ollama pull mistral). Open Customisable_AI_Chabbot.py in your code editor. Locate the ask_llama function on line 11. Change the model="llama3.2" argument to match your downloaded model (e.g., model="mistral").