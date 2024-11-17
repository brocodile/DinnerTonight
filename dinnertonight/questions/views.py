import requests
from django.shortcuts import render
from .forms import UserPreferencesForm
from dotenv import load_dotenv
from os import getenv

# Load environment variables from a .env file
load_dotenv()
HF_API_TOKEN = getenv('API_KEY')

# Hugging Face Inference API endpoint for text generation
HF_API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"

# Function to call Hugging Face API for text generation
def generate_bio(input_text):
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
    }
    payload = {"inputs": input_text}

    try:
        response = requests.post(HF_API_URL, json=payload, headers=headers)
        response.raise_for_status()

        # Extract generated text and include everything from "I am" onward
        generated_text = response.json()[0]['generated_text']
        start_idx = generated_text.find("I am")
        if start_idx != -1:
            text = generated_text[start_idx:]
            text = text.split(". ")
            text[-1] = ""
            cleaned_text = ". ".join(text)
            return cleaned_text
        else:
            return "Error: Generated text"
    except requests.exceptions.RequestException:
        return "Error generating text."

# Main view to handle the form and generate bio
def questions(request):
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Prepare input text based on the form data
            input_text = (
                f"Write a creative, engaging bio in 3-4 sentences for a social media profile, "
                f"about a {data['personality_traits']} {data['career']}. "
                f"Their interests include {data['interests']}, and they are seeking a {data['relationship_goals']} relationship. "
                f"Start the answer with - I am"
            )

            # Generate a bio using the Hugging Face API
            bio = generate_bio(input_text)

            # Pass the generated bio and form data to the success template
            return render(request, 'questions/success.html', {'data': data, 'bio': bio})
    else:
        form = UserPreferencesForm()

    return render(request, 'questions/questions.html', {'form': form})