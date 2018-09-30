# Django
from django import forms
from django.conf.urls import url
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse

# Other
import json
import requests
