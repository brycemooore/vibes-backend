from django.contrib import admin


from .models import User, Song

admin.site.register(User)
admin.site.register(Song)
# Register your models here.
