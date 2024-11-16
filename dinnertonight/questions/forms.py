from django import forms

class UserPreferencesForm(forms.Form):
    CAREER_CHOICES = [
        ('software_engineer', 'Software Engineer'),
        ('author', 'Author'),
        ('teacher', 'Teacher'),
        ('designer', 'Designer'),
        ('artist', 'Artist'),
        ('entrepreneur', 'Entrepreneur'),
        ('chef', 'Chef'),
        ('musician', 'Musician'),
    ]

    INTEREST_CHOICES = [
        ('cooking', 'Cooking'),
        ('painting', 'Painting'),
        ('cycling', 'Cycling'),
        ('hill_climbing', 'Hill Climbing'),
        ('traveling', 'Traveling'),
        ('fitness', 'Fitness'),
        ('music', 'Music'),
        ('literature', 'Literature'),
        ('technology', 'Technology'),
        ('gaming', 'Gaming'),
        ('movies', 'Movies'),
    ]

    TRAIT_CHOICES = [
        ('adventurous', 'Adventurous'),
        ('creative', 'Creative'),
        ('compassionate', 'Compassionate'),
        ('outgoing', 'Outgoing'),
        ('introverted', 'Introverted'),
        ('homely', 'Homely'),
        ('sentimental', 'Sentimental'),
    ]

    RELATIONSHIP_CHOICES = [
        ('casual', 'Casual'),
        ('long_term', 'Long-term'),
        ('adventurous', 'Adventurous'),
        ('deep_connection', 'Seeking Deep Connection'),
    ]

    # Define dropdown fields
    career = forms.ChoiceField(choices=CAREER_CHOICES, label="Career/Profession")
    interests = forms.ChoiceField(choices=INTEREST_CHOICES, label="Interests")
    personality_traits = forms.ChoiceField(choices=TRAIT_CHOICES, label="Personality Traits")
    relationship_goals = forms.ChoiceField(choices=RELATIONSHIP_CHOICES, label="Relationship Goals")
