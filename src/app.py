import os
from dotenv import load_dotenv
from email_utils import send_email_gmail
from yaml import safe_load
from model_utils import call_ollama

_ = load_dotenv('../.env',override=True)

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')

CONFIG = safe_load(open(CONFIG_PATH, 'r'))
MODEL_NAME = CONFIG['model']['name']
if __name__ == "__main__":

    model_name = MODEL_NAME  # Change to the model you have pulled in Ollama
    user_prompt = "Write a short Python function to reverse a string."
    
    result = call_ollama(model_name, user_prompt)
    print("Ollama Response:\n", result)

    sender = os.environ.get('GMAIL_USER')
    app_password = os.environ.get('GMAIL_PASSWORD')
    recipient = os.environ.get('EMAIL_RECIPIENT')
    subject = "Test Email from Python"
    body = result

    # send_email_gmail(sender, app_password, recipient, subject, body)

