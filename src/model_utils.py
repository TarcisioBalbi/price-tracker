import requests
import json

def call_ollama(model: str, prompt: str) -> str:
    """
    Calls a local Ollama model and returns the generated text.
    
    Args:
        model (str): Name of the Ollama model (e.g., 'llama2', 'mistral', 'codellama').
        prompt (str): The input text prompt.
    
    Returns:
        str: The generated text from the model.
    """
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # Set to True for streaming responses
    }

    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except requests.exceptions.RequestException as e:
        return f"Error calling Ollama API: {e}"
    except json.JSONDecodeError:
        return "Error: Invalid JSON response from Ollama."
