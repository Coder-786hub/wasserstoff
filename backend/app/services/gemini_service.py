import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyD8FrLR6bmeG6NFEztRtvdfoPH-FGIkaHc")

def run_gemini_prompt(prompt, context=None):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([context, prompt] if context else [prompt])
    return response.text
