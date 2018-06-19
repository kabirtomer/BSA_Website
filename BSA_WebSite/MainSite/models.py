from django.db import models

# Create your models here.

TEAMS = (
    ('', 'None'),
    ('Athletics (Men)', 'Athletics (Men)'),
    ('Athletics (Women)', 'Athletics (Women)'),
    ('Aquatics (Men)', 'Aquatics (Men)'),
    ('Aquatics (Women)', 'Aquatics (Women)'),
    ('Badminton (Men)', 'Badminton (Men)'),
    ('Badminton (Women)', 'Badminton (Women)'),
    ('Basketball (Men)', 'Basketball (Men)'),
    ('Basketball (Women)', 'Basketball (Women)'),
    ('Cricket', 'Cricket'),
    ('Football', 'Football'),
    ('Hockey', 'Hockey'),
    ('Lawn Tennis (Men)', 'Lawn Tennis (Men)'),
    ('Lawn Tennis (Women)', 'Lawn Tennis (Women)'),
    ('Squash', 'Squash'),
    ('Table Tennis (Men)', 'Table Tennis (Men)'),
    ('Table Tennis (Women)', 'Table Tennis (Women)'),
    ('Volleyball (Men)', 'Volleyball (Men)'),
    ('Volleyball (Women)', 'Volleyball (Women)'),
    ('Weight-lifting', 'Weight-lifting')
)


class People(models.Model):
    Secretary = 'secy'
    Executive = 'exe'
    Faculty = 'fac'
    Captain = 'cap'
    ViceCaptain = 'vicecap'
    people_types = (
        (Secretary, 'Secretary'),
        (Executive, 'Executive'),
        (Faculty, 'Faculty'),
        (Captain, 'Captain'),
        (ViceCaptain, 'Vice-Captain')
    )
    type = models.CharField(blank=False, max_length=8, choices=people_types, default=Secretary)
    team = models.CharField(blank=True, max_length=20, choices=TEAMS, default='', help_text="Leave blank if not capn or vice-capn")
    name = models.CharField(blank=False, max_length=30, help_text="Full Name")
    entryno = models.CharField(blank=True, max_length=15, help_text="Leave Blank if faculty")
    mobileno = models.CharField(blank=True, max_length=15, help_text="Mobile Number")
    email = models.CharField(blank=False, max_length=30, help_text="Email ID")
    hostel = models.CharField(blank=True, max_length=15, help_text="Leave Blank if faculty")
    fb = models.CharField(blank=True, max_length=200, help_text="Not required")
    image_link = models.CharField(blank=False, max_length=500)


class Event(models.Model):
    name = models.CharField(blank=False, max_length=50)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=True)
    short_des = models.CharField(blank=True, max_length=300)
    long_des = models.TextField
    logo_link = models.CharField(blank=True, max_length=500)
    image_link = models.CharField(blank=True, max_length=500)


class Gallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    path_to_images = models.CharField(blank=False, max_length=500)


class Announcement(models.Model):
    desc = models.CharField(blank=False, max_length=300)
    link = models.CharField(blank=True, max_length=500)


class LiveMatch(models.Model):
    score = models.CharField(blank=False, max_length=100)
    start_time = models.DateTimeField('time started')
    duration = models.TimeField
    header = models.CharField(blank=False, max_length=500)
    end_text = models.CharField(blank=True, max_length=500)


class Comment(models.Model):
    LiveMatch = models.ForeignKey(LiveMatch, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
