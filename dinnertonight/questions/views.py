from django.shortcuts import render
from .forms import UserPreferencesForm
from transformers import pipeline

# Load the Hugging Face text-generation pipeline
text_generator = pipeline("text-generation", model="gpt2") # can use different models

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

            # Generate a bio using Hugging Face
            generated = text_generator(input_text, max_length=50, num_return_sequences=1)
            bio = generated[0]['generated_text']

            # Pass the generated bio and form data to the success template
            return render(request, 'questions/success.html', {'data': data, 'bio': bio})
    else:
        form = UserPreferencesForm()

    return render(request, 'questions/questions.html', {'form': form})
