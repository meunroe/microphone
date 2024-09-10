from typing import Any
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import ShopUser

class ShopUserLoginForm(AuthenticationForm):
  class Meta:
    model = ShopUser
    fields = ('username', 'password')

  def __init__(self, *args, **kwargs):
    super(ShopUserLoginForm, self).__init__(*args, **kwargs)
    self.fields["username"].widget.attrs["placeholder"] = "login"
    self.fields["password"].widget.attrs["placeholder"] = "password"
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'input_admin_login'

class ShopUserRegistrForm(UserCreationForm):
  class Meta:
    model = ShopUser
    fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar')
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    placeholder_list = {'username':'username', 'first_name':'first_name', 'password1':'password', 'password2':'password again', 'email':'email', 'age':'age', 'avatar':'avatar'}
    for name, placeholder in placeholder_list.items():
      self.fields[name].widget.attrs["placeholder"] = placeholder
    for fieald_name, field in self.fields.items():
      field.widget.attrs['class'] = 'menu_item_element'
      field.help_text = ''
  
  # def clean_age(self):
  #   data = self.cleaned_data['age']
  #   if data < 18:
  #     raise forms.ValidationError("Вы слишком молоды!")
  #   return data

    