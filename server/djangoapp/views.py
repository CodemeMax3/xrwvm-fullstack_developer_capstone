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
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']

        user = authenticate(username=username, password=password)
        response = {"userName": username}

        if user is not None:
            login(request, user)
            response = {"userName": username, "status": "Authenticated"}

        return JsonResponse(response)

    return JsonResponse({"error": "Invalid request"})


# ------------------ LOGOUT ------------------
@csrf_exempt
def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})


# ------------------ REGISTRATION ------------------
@csrf_exempt
def registration(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        first_name = data.get('firstName', '')
        last_name = data.get('lastName', '')
        email = data.get('email', '')

        try:
            User.objects.get(username=username)
            return JsonResponse({"userName": username, "error": "Already Registered"})
        except:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            login(request, user)

            return JsonResponse({
                "userName": username,
                "status": "Authenticated"
            })

    return JsonResponse({"error": "Invalid request"})


# ------------------ HOME ------------------
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