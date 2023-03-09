from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import User

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def sign_in(request):
    print(request.POST['first_name'])
    return HttpResponse('hello signin')