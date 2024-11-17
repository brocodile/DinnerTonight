import requests
from django.shortcuts import render
from .forms import UserPreferencesForm
from dotenv import load_dotenv
from os import getenv

# Load environment variables from a .env file
load_dotenv()
# Replace with your Hugging Face API token
HF_API_TOKEN = getenv('API_KEY')

# Hugging Face Inference API endpoint for text generation
HF_API_URL = "https://api-inference.huggingface.co/models/gpt2"  # You can use a different model if needed

# Function to call Hugging Face API for text generation
def generate_bio(input_text):
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
    }
    payload = {
        "inputs": input_text,
        "parameters": {
            "max_length": 50,  # Adjust this as per your needs
            "num_return_sequences": 1,
        }
    }

    response = requests.post(HF_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return "Error generating text."

def questions(request):
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Prepare input text based on the form data
            input_text = (
                f"A {data['personality_traits']} individual with a career as a {data['career']} and interests in {data['interests']}."
                f" They are looking for {data['relationship_goals']}."
            )

            # Generate a bio using Hugging Face API
            bio = generate_bio(input_text)

            # Pass the generated bio and form data to the success template
            return render(request, 'questions/success.html', {'data': data, 'bio': bio})
    else:
        form = UserPreferencesForm()

    return render(request, 'questions/questions.html', {'form': form})