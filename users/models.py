from django.db import models
from django.contrib.auth.models import User
from PIL import Image # image resize korar jonno

# Create your models here.
class Profile(models.Model):
    #one to one relationship with the existing user model
    user = models.OneToOneField(User, on_delete=models.CASCADE) # , null=True, blank=True
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')#

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self):
        # model save houar shathe shathe ei method ta run hobe
        #parent class e ei method ta already ase .. but amra  amader moto abar create kortesi.. jeno amra kichu functionality add korte pari
        super().save() # parent class er save method ta run korlam

        img = Image.open(self.image.path) # image ta profile instance er jonno open korlam
        if  img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) ## image ta ke resize korlam
            img.save(self.image.path) ## then image ta save korlam.. same path e save korlam, in order to overwrite that large image





