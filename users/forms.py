from django import forms
from django.contrib.auth.models import User # import User model
from django.contrib.auth.forms import UserCreationForm #
from .models import Profile


# now we create a new form that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm): # inherit korlam
    # ekhon additional field create korbo
    email = forms.EmailField() # required = False , default -> required = True

    class Meta: # this class gives us nested namespace for configuration
        # and keeps these configuration in one place.. and within the configuration
        # we are saying that the model would be effected is the User model
        # example , when we are going to save the form .. from.save -> its going to save it to this User model
        # We are going to specify the model that we want this form interrect with
        model = User # cz, whenever this form validate, its going to create a new user
        fields = ['username', 'email', 'password1', 'password2']
        # these are the fields which are going to be shown on our form
        # oder set hoye jabe

    # ekhon view e amra ei form ta use korte parbo .. UserCreationForm er bodol e


    ##### LV-23 ## User Profile update korar jonno form create korbo ekhon..

    # we are gonna create something called model form. And a model form allows us to
    # create a form that will work with a specific database model. And in this case
    # we want a form that will update our user model. lets create this

class UserUpdateForm(forms.ModelForm): # forms.ModelForm theke inherit korlam
    # this is gonna very simmilar to our user register form except amra ekhane password form use korbo na ..
    # so, amra shudhu User Name and email update korte chai..
    class Meta:
        model = User
        fields = ['username', 'email']
        # future e amader request password form dorkar hobe .. where they can request a reset email for the password
        # ekhane profile picture nia amra kaj kori nai
        # Profile model e amra Profile picture nia kaj korbo.. User Model e na..
        # So, we actually need to create an additional form..
        # since we will be working with the profile model, First we need to import that

# Profile model ta import korar pore .. ekhon amra profile form nia kaj korte parbo
class ProfileUpdateForm(forms.ModelForm): #
    # amra ekhane kono additional field add korbo na ..
    class Meta:
        model = Profile # jei model nia amra kaj korbo .. sheta hocche Profile
        fields = ['image'] # ar jei field nia amra kaj korbo .. sheta hocche image  # 'image' [] er moddhe add korte hobe


# so apatoto amader 2 ta form holo eibar.. ekta userUpdateForm.. arekta profileUpdateForm
#UserForm allow us to update our User Name and email.. And the profile form allow us to update our image

# whenever we actually put this on the template.. its going to look like just one form
# ekhon profile view e ei form gula add korte hobe












