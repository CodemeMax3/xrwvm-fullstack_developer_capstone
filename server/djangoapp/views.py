from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from datetime import datetime
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate

# Logger
logger = logging.getLogger(__name__)

# ------------------ LOGIN ------------------
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)
    data = {"userName": username}

    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}

    return JsonResponse(data)


# ------------------ LOGOUT ------------------
@csrf_exempt
def logout_request(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)


# ------------------ REGISTRATION ------------------
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data.get('firstName', '')
    last_name = data.get('lastName', '')

    try:
        user = User.objects.get(username=username)
        return JsonResponse({"userName": username, "error": "Already Exists"})
    except:
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        return JsonResponse({"userName": username})


# ------------------ HOME / DEALERS ------------------
def get_dealerships(request):
    return render(request, "Home.html")


# ------------------ DEALER REVIEWS ------------------
def get_dealer_reviews(request, dealer_id):
    return render(request, "DealerDetails.html", {"dealer_id": dealer_id})


# ------------------ DEALER DETAILS ------------------
def get_dealer_details(request, dealer_id):
    return render(request, "DealerDetails.html", {"dealer_id": dealer_id})


# ------------------ ADD REVIEW ------------------
@csrf_exempt
def add_review(request):
    if request.method == "POST":
        return JsonResponse({"status": "Review Added"})