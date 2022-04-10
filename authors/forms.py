
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm,
)

from django.forms import CharField, TextInput, PasswordInput

class RegisterUserForm(UserCreationForm):

    username = CharField(
        widget=TextInput(attrs={'min_length': 6, 'max_length': 20})
    )

    password1 = CharField(
        widget=PasswordInput(attrs={'min_length': 7, 'max_length': 12})
    )

    password2 = CharField(
        widget=PasswordInput(attrs={'min_length': 7, 'max_length': 12})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for label, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "widget_style user_form_input"}
            )
            if label == "password2":
                field.widget.attrs.update({"disabled": True})

    def __str__(self):
        return f"{self.__class__.__name__}"





class LoginUserForm(AuthenticationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for label, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "widget_style user_form_input"}
            )

    def __str__(self):
        return f"{self.__class__.__name__}"
