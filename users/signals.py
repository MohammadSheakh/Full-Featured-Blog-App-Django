from django.db.models.signals import post_save # this is a signal that gets fired
# after an object is saved
from django.contrib.auth.models import User # user model tai holo sender
from django.dispatch import receiver
# A receiver is going to be a function that that gets this signal and perfoms some task
from .models import Profile
# import profile from model .. since we creating a profile in our function

    # so the reason we are doing this .. cz,  we want a user profile, to be created for each new user

#DETAILS : LV-22
# Jekono user create hoilei ei function ta kaj korbe
@receiver(post_save, sender=User) # when a user is saved then send this post_save signal.. and that signal is going to received by the receiver.. ar ei receiver tai holo create_profile function..
def create_profile(sender, instance, created, **kwargs): # function takes all of these arguments.. jegula post_save signal pass korse.. er moddhe ekta hocche instance of the User... arekta hocche created
    if created:
        Profile.objects.create(user=instance) # so we are saying .. if the user is created then create a profile object with the user = the instance of the user.. that was created

# save_profile function.. saves our profile.. everytime the user object get saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): # function er sheshe onno kono argument ashle last er keyword ta sheta accept kore ..
    instance.profile.save() # user save korlei profile ta save hobe

