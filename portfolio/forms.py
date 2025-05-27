# portfolio/forms.py
from django import forms
from .models import About, Skill, Certificate, Project, Experience, Education, Learning, Activity

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['content']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'issued_by', 'date_issued']
        widgets = {
            'date_issued': forms.DateInput(attrs={'type': 'date'})
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'technologies_used', 'project_link', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['role', 'company', 'description', 'start_date', 'end_date', 'location']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_year', 'end_year', 'description']

class LearningForm(forms.ModelForm):
    class Meta:
        model = Learning
        fields = ['topic', 'status', 'description']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'content', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }