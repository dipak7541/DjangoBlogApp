from django import forms
from blogs.models import AutherRegistration, BlogModel

class AutherRegistrationForm(forms.ModelForm):
    password=forms.CharField(max_length=150,widget=forms.PasswordInput())
    confrompassword=forms.CharField(max_length=150,widget=forms.PasswordInput())

    class Meta:
        model = AutherRegistration
        fields=["profileimage","username","first_name","middle_name","last_name","email","gender","password"]

    def clean(self):
        cleaned_data = super(AutherRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confrompassword")
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    def save(self, commit=True):
        # Save the provided password in hashed format
        auther = super(AutherRegistrationForm, self).save(commit=False)
        auther.set_password(self.cleaned_data["password"])
        if commit:
            auther.save()
        return auther

class LoginForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(max_length=128,widget=forms.PasswordInput())

class BlogDataForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields=["tittle", "description"]