from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
import datetime
from .models import User, Trip, Trip_Join

# Create your views here.
def index(request):
    return render(request, 'pythonBlackBeltApp/index.html')

def login(request):
    if request.method == "POST":
        result = User.userMgr.login(
            username       =   request.POST['username'],
            password    =   request.POST['password']
        )
        if result[0]:
            request.session['user_id'] = result[1].id
            request.session['user_name'] = result[1].name
            return redirect(reverse('dashboard'))
        else:
            for error in result[1]:
                messages.add_message(request, messages.INFO, result[1][error])
            return redirect(reverse('index'))
    else:
        return redirect(reverse('index'))

def register(request):
    if request.method == "POST":
        result = User.userMgr.register(
            name  =   request.POST['name'],
            username   =   request.POST['username'],
            email       =   request.POST['email'],
            password    =   request.POST['password'],
            confirm_pw  =   request.POST['confirm_pw']
        )
        if result[0]:
            request.session['user_id'] = result[1].id
            request.session['user_name'] = result[1].name
            return redirect(reverse('dashboard'))
        else:
            for error in result[1]:
                messages.add_message(request, messages.INFO, result[1][error])
            return redirect(reverse('index'))
    else:
        return redirect(reverse('index'))

def dashboard(request):
    availableTrips = []

    user = User.userMgr.get(id=request.session['user_id'])
    availableTrips = Trip.objects.order_by('start_date')

    context = {
        'user' : user,
        'trips' : Trip.objects.filter(user=user),
        'attending' : Trip_Join.objects.filter(attendee=user),
        'othersTrips' : availableTrips
    }
    return render(request, 'pythonBlackBeltApp/travels.html', context)

def join(request, id):
    user = User.userMgr.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=id)
    Trip_Join.objects.create(trip=trip, attendee=user)

    messages.add_message(request, messages.INFO, 'You are joining trip ' + str(id))
    return redirect(reverse('dashboard'))

def add(request):
    return render(request, 'pythonBlackBeltApp/add.html')

def add_travel(request):
    for field in request.POST:
        if len(request.POST[field]) < 1:
            messages.add_message(request, messages.INFO, 'All fields are required!')
            return redirect(reverse('add'))
            break
    try:
        startDate = datetime.datetime.strptime(request.POST['start_date'],'%m/%d/%Y')
        endDate = datetime.datetime.strptime(request.POST['end_date'],'%m/%d/%Y')

        if startDate < datetime.datetime.now():
            messages.add_message(request, messages.INFO, 'Start Date must be after today. Must be in MM/DD/YYYY format.')
            return redirect(reverse('add'))
        elif startDate > endDate:
            messages.add_message(request, messages.INFO, 'End Date must be after Start Date. Must be in MM/DD/YYYY format.')
            return redirect(reverse('add'))
    except Exception,e:
        messages.add_message(request, messages.INFO, 'The dates entered are invalid. Must be in MM/DD/YYYY format.')
        return redirect(reverse('add'))


    user = User.userMgr.get(id=request.session['user_id'])
    Trip.objects.create(user=user, destination=request.POST['destination'], start_date=startDate, end_date=endDate, plan=request.POST['description'])
    return redirect(reverse('dashboard'))

def trip_detail(request, id):
    attendees = None
    try:
        attendees = Trip_Join.objects.filter(trip=id)
    except:
        pass

    context = {
        "trip" : Trip.objects.get(id=id),
        "attendees" : attendees
        }
    return render(request, 'pythonBlackBeltApp/trip_detail.html', context)

def logout(request):
    request.session.pop('user_id')
    request.session.pop('user_name')
    return redirect(reverse('index'))
