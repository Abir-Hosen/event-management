
from .models import Volunteer

from rest_framework import serializers

class VolunteerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['id', 'first_name', 'last_name', 'preferred_name', 'email', 'phone', 'zip', 'city', 'state', 'country',
                  'fb_link', 'dob', 'experience', 'experience_description', 'current_job', 'qualifications', 'about',
                  'comments', 'preferred_tasks', 'preferred_tasks_info', 'preferred_time_frame',
                  'volunteering_with_friends', 'volunteering_with_head', 'dept_head_name', 'emg_first_name',
                  'emg_last_name', 'emg_relation_name', 'emg_phone', 'active']
