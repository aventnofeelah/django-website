from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        User = get_user_model() 
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        User = get_user_model()  
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None