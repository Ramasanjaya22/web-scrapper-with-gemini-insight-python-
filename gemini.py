"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import google.generativeai as genai

def initialize_gemini_model(api_key):
    genai.configure(api_key=api_key)

    generation_config = {
        "temperature": 0.5,  # Adjust for creativity (0 = deterministic, 1 = most creative)
        "top_p": 0.95,       # Nucleus sampling for diversity
        "top_k": 40,         # Consider top 40 most likely words
    }
    safety_settings = [
      {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
      {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
      {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
      {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
      ]
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        safety_settings=safety_settings,
        system_instruction="Application For Job Categories Scedule",
    )
    return model.start_chat()

def generate_gemini_response(chat_session, prompt):
  response = chat_session.send_message(prompt)
  return response.text
