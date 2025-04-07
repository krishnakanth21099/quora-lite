from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Question, Answer

class UserRegistrationForm(UserCreationForm):
    """
    Custom user registration form extending Django's UserCreationForm.

    This form allows users to register with additional fields:
    - Email (made required)
    - First name
    - Last name
    - Profile icon

    Inherits password validation and creation logic from UserCreationForm.

    Attributes:
        username (CharField): Input field for username
        email (EmailField): User's email address (made required)
        password1 (CharField): Password field (first password)
        password2 (CharField): Password confirmation field
        first_name (CharField): Input field for first name
        last_name (CharField): Input field for last name
        icon (ImageField): Input field for profile icon

    Meta:
        model (User): Custom User model
        fields (list): Fields to be included in the form
    """
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'icon']

class QuestionForm(forms.ModelForm):
    """
    Form for creating new questions.

    Allows users to input a title and description for a new question.

    Attributes:
        title (CharField): Input field for question title
        description (CharField): Textarea for detailed question description

    Meta:
        model (Question): Question model from the database
        fields (list): Fields to be included in the form
        widgets (dict): Custom form widget configurations
    """
    class Meta:
        model = Question
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class AnswerForm(forms.ModelForm):
    """
    Form for submitting answers to questions.

    Allows users to provide a text-based answer to a specific question.

    Attributes:
        content (CharField): Textarea for answer content

    Meta:
        model (Answer): Answer model from the database
        fields (list): Fields to be included in the form
        widgets (dict): Custom form widget configurations
    """
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
