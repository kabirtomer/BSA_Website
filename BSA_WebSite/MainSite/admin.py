from django.contrib import admin
from .models import People, Event, Announcement, LiveMatch, Comment, Gallery

# Register your models here.

admin.site.register(People)
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(Announcement)
admin.site.register(LiveMatch)
admin.site.register(Comment)
