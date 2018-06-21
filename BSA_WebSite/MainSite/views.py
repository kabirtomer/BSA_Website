from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import People, Event, Gallery, Announcement, LiveMatch, Comment
import os
# Create your views here.

"""DECLARE LINK TO STATIC DISPLAY IMAGES HERE"""
STATIC_DIR = 'static'
SHOWCASE_DIR = 'showcase'
""" END"""

Secretary = 'secy'
Executive = 'exe'
Faculty = 'fac'
Captain = 'cap'
ViceCaptain = 'vicecap'
MAX_RECENT_MATCHES = 5


def index(request):
    announcements = Announcement.objects.all()
    live_matches = []
    upcoming_matches = []
    for match in LiveMatch.objects.all():
        if match.start_time > datetime.now() - match.duration:
            live_matches.append(match)
        elif match.start_time > datetime.now():
            upcoming_matches.append(match)
    context = {'announcements': announcements, 'live_matches': live_matches, 'upcoming_matches': upcoming_matches}
    return render(request, 'MainSite/index.html', context)


def people(request):
    faculty_list = People.objects.filter(type=Faculty)
    secretaries = People.objects.filter(type=Secretary)
    executives = People.objects.filter(type=Executive)
    team_members = People.objects.filter(type=Captain or ViceCaptain).order_by('team')
    context = {'faculty_list': faculty_list, 'secretaries': secretaries, 'executives': executives,
               'team_members': team_members}
    return render(request, 'MainSite/people.html', context)


def events(request):
    date = datetime.today()
    day_events = Event.objects.filter(date=date)
    past_events = Event.objects.filter(date__lt=date)
    upcoming_events = Event.objects.filter(date__gt=date)
    context = {'day_events': day_events, 'past_events': past_events, 'upcoming_events': upcoming_events}
    return render(request, 'MainSite/events.htmL', context)


def gallery(request):
    all_event_images = []
    showcase_images = []
    for root, dirs, files in os.walk(os.path.join(STATIC_DIR, SHOWCASE_DIR)):
        for filename in files:
            showcase_images.append(filename)
    showcase = {
        "base_dir": SHOWCASE_DIR,
        "images": showcase_images
    }
    for item in Gallery.objects.all():
        images = []
        for root, dirs, files in os.walk(os.path.join(STATIC_DIR, item.path_to_images)):
            for filename in files:
                images.append(filename)
        event = {
            "event_name": item.event.name,
            "base_dir": item.path_to_images,
            "images": images
        }
        all_event_images.append(event)
    return render(request, 'MainSite/gallery.htmL', {'all_event_images': all_event_images, 'showcase': showcase,
                                                     "static_dir": STATIC_DIR})


def live(request):
    live_matches = []
    temp = []
    upcoming_matches = []
    for match in LiveMatch.objects.all():
        if match.start_time > datetime.now() - match.duration:
            live_matches.append(match)
        elif match.start_time > datetime.now():
            upcoming_matches.append(match)
        else:
            temp.append()
    comments = {}
    for match in live_matches:
        comments[match.header] = match.comment_set.all()
    recent_matches = []
    for match in temp:
        if match.start_time > datetime.now() - timedelta(days=7):
            recent_matches.append(match)
    context = {'upcoming_matches': upcoming_matches, 'live_matches': live_matches, 'recent_matches': recent_matches, 'comments': comments}
    return render(request, 'MainSite/live.htmL', context)



