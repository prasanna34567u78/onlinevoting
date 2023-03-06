from django.contrib import admin
from .models import Votes,Position,Candidate,Voter
# Register your models here.
admin.site.register(Voter)
admin.site.register(Position)
admin.site.register(Candidate)
admin.site.register(Votes)