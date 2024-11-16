from django.shortcuts import render
from .forms import UserPreferencesForm  # Import the form
# Create your views here.

def questions(request):
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST)
        if form.is_valid():
            # Process the form data
            data = form.cleaned_data
            return render(request, 'questions/success.html', {'data': data})  # Redirect to success page
    else:
        form = UserPreferencesForm()  # Display an empty form for GET requests

    return render(request, 'questions/questions.html', {'form': form})

