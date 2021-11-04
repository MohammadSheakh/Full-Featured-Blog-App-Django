from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User # so the post model and the user model are going to have a relationship, since user are going to author post
#Specifically this is going to be called a one to many relationship
#cz, one user can have multiple post, but a post can only have one author
#django te ei kaj ta korar jonno foreign key use korte hoy

# Create your models here.

# Users -> Author of the post
# create new user model
# custom field to user model

# ekhon amra ekta post model create korbo .. eta ekta class that inherits from django model class

# each class is going to be its own table and database
class Post(models.Model):
    # ekhon amra kichu attribute create korbo, prottekta attribute, database er different field hobe
    title = models.CharField(max_length=100)
    content = models.TextField() # unrestricted text.. many lines
    date_posted = models.DateTimeField(default=timezone.now) # auto_now=True  auto_now_add=True

    # we also need author for each post.. this will be the user .. who create the post
    # user er separate table dorkar
    # prothom e user model import kore nite hobe .. django eta create kore thake

    author = models.ForeignKey(User, on_delete=models.CASCADE) # author jei post gula create korse ..
    # ekhon shei author e delete hoye gele ... hoyto post gulao delete hoye jabe .. or post er author er value none set hoye jabe
    #CASCADE use korar maddhome .. user delete hoye gele .. post o delete hoye jabe

    def __str__(self):
        return self.title


    # we need to create getAbsoluteUrl Method .. so that django knows .. how to find a location to specific post ..
    # so first we are going to be getting the URL of a particular route .. and in order to do this .. we need to use the reverse function..
    # ekhon kotha hocche amra keno redirect function use korbo na .. redierect .. amader ke specific route e redirect kore ..
      # but reverse will simply return the full URL .. to the Route as a String

    # ei problem er khetre amra .. ekhan theke return the URL as String ... ar .. view ke amader jonno redirect korte dibo ..

    def get_absolute_url(self): # this method will tell django .. how find the URL to in specific instance of a post
        return reverse('post-detail', kwargs={'pk': self.pk}) # return the path to specific post
        # reverse will return full path as String

        #jar full path amra chai...path to  post-detail  route .. it needs specific post with a primary key ..  Url parameter called pk .. Primary key

        #amra jodi specific post er bodole home page e move korte chai .. taile Create View e amader ekta attribute set korte hobe .. sheta holo
                       # Success URL .. eta te home page link kore dite hobe .. tailei hobe.. amader case e amra detail view e dekhaitesi














