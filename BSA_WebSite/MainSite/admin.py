from django.contrib import admin
from .models import People, Events, Announcements, LiveMatch, Comment

# Register your models here.

admin.site.register(People)
admin.site.register(Events)
admin.site.register(Announcements)
admin.site.register(LiveMatch)
admin.site.register(Comment)
