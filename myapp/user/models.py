from django.db import models


# Create your models here.


class Permission(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # all
    create_all = models.BooleanField()
    read_all = models.BooleanField()
    update_all = models.BooleanField()
    delete_all = models.BooleanField()
    # user
    create_user = models.BooleanField()
    read_user = models.BooleanField()
    update_user = models.BooleanField()
    delete_user = models.BooleanField()
    # event
    create_event = models.BooleanField()
    read_event = models.BooleanField()
    update_event = models.BooleanField()
    delete_event = models.BooleanField()
    # ticket
    create_ticket = models.BooleanField()
    read_ticket = models.BooleanField()
    update_ticket = models.BooleanField()
    delete_ticket = models.BooleanField()
    # volunteer
    create_volunteer = models.BooleanField()
    read_volunteer = models.BooleanField()
    update_volunteer = models.BooleanField()
    delete_volunteer = models.BooleanField()
    # sales_n_report
    create_sales_n_report = models.BooleanField()
    read_sales_n_report = models.BooleanField()
    update_sales_n_report = models.BooleanField()
    delete_sales_n_report = models.BooleanField()
    # mail
    create_email = models.BooleanField()
    read_email = models.BooleanField()
    update_email = models.BooleanField()
    delete_email = models.BooleanField()


class Role(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # permission
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)



class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    event_creator = models.BooleanField(default=False, null=True)
    # roles
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, null=True)


class Address(models.Model):
    name: models.CharField(max_length=200)
    address_line_one = models.CharField(max_length=200)
    address_line_two = models.CharField(max_length=200)
    zip: models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    google_map_url = models.URLField(max_length=200)
    # user
    user= models.ForeignKey(User, on_delete=models.DO_NOTHING)

