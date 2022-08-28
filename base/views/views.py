from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from ..forms import CreateUserForm, FoodForm, ExerciseForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ..models import *

#pagination imports:

from django.core.paginator import Paginator

