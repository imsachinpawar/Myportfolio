# portfolio/admin.py
from django.contrib import admin
from .models import About, Skill, Certificate, Project, Experience, Education, Learning, Activity

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Certificate)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Learning)
admin.site.register(Activity)