from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.user.username

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    MS_CHOICES = (
        ("FACEBOOK", "FACEBOOK"),
        ("INSTAGRAM","INSTAGRAM"),
        ("TWITTER","TWITTER"),
        ("OTHERS","OTHERS"),
    )
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    register_timestamp = models.DateTimeField(auto_now_add=True)
    regidter_update = models.DateTimeField(auto_now=True)
    frist_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField()
    personal_email = models.EmailField()
    cell_phone = models.CharField(max_length=10, blank=True)
    local_phone = models.CharField(max_length=10, blank=True)
    marketing_strategy = models.CharField(max_length=32, choices = MS_CHOICES)
    contacted = models.BooleanField(default=False)
    captured = models.BooleanField(default=False)

    class Meta:
        pass
        #ordering = ["register_timestamp"]

    def __str__(self):
        return self.frist_name

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender = User)

