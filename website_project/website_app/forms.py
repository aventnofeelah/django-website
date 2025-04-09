from django import forms 
from .models import Users, Works
from django.contrib.auth.password_validation import validate_password
import re

class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = Users
        fields = ['username', 'email', 'country', 'password']
        labels = {
            'username' : 'Username:', 'email' : 'Email:', 'country' : 'Country:', 'password' : 'Password:'
        }
        widgets = {
            'password' : forms.PasswordInput(),
            'email' : forms.EmailInput(attrs={'required' : True})
        }

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     validate_password(password)
    #     return password
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        if Users.objects.filter(email = email).exists():
            raise forms.ValidationError('This email already exists.')
        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match.')
        if not re.match(r'^[a-zA-Z0-9]+$', username):
            raise forms.ValidationError('Please use only latin characters.')
        symbols = ['!', '@', '#', '%', '^', '*', '(', ')', ';', '"', "'", ',', '.', ' ']
        for x in symbols:
            if x in username:
                raise forms.ValidationError(f'{x} is invalid symbol.')
        validate_password(password)
        
        return cleaned_data

class AddPortfolioForm(forms.ModelForm):
    class Meta: 
        model = Works
        fields = ['name', 'speciality', 'screenshots', 'files', 'description']
        labels = {
            'name' : 'Porfolio title', 'speciality' : 'Speciality', 'screenshots' : 'Screenshots', 'files' : 'Files', 'description' : 'Description'
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user and hasattr(user, 'profession'):
            self.fields['speciality'].initial = user.profession 

class SearchUserForm(forms.Form):
    query = forms.CharField(max_length=20, required=False, label='',
                            widget=forms.TextInput(attrs={
                                'id' : 'search-users-input',
                                'placeholder' : 'Search user'
                            }))
    





        

    
