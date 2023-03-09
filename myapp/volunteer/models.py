from django.db import models
from user.models import User


# Create your models here.
class Volunteer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    preferred_name = models.CharField(max_length=200, blank=True, null=True)

    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200, unique=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    fb_link = models.CharField(max_length=200)
    dob = models.DateField(blank=True, null=True)
    experience = models.CharField(max_length=200)
    experience_description = models.CharField(max_length=2000)
    current_job = models.CharField(max_length=200)
    qualifications = models.CharField(max_length=200)
    about = models.CharField(max_length=2000, blank=True, null=True)
    comments = models.CharField(max_length=2000, blank=True, null=True)
    preferred_tasks = models.CharField(max_length=200)
    preferred_tasks_info = models.CharField(max_length=2000, blank=True, null=True)
    preferred_time_frame = models.CharField(max_length=200)
    volunteering_with_friends = models.CharField(max_length=200, blank=True, null=True)
    volunteering_with_head = models.BooleanField(blank=True, null=True)
    dept_head_name = models.CharField(max_length=200, blank=True, null=True)
    emg_first_name = models.CharField(max_length=200)
    emg_last_name = models.CharField(max_length=200, blank=True, null=True)
    emg_relation_name = models.CharField(max_length=200)
    emg_phone = models.CharField(max_length=200)

    active = models.BooleanField(default=False)

    # common for all
    created = models.DateTimeField(auto_now_add=True)
    # user
    user= models.OneToOneField(User, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['created']
