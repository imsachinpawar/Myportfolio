# portfolio/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AboutViewSet, SkillViewSet, CertificateViewSet, ProjectViewSet,
    ExperienceViewSet, EducationViewSet, LearningViewSet, ActivityViewSet
)

router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'education', EducationViewSet)
router.register(r'learning', LearningViewSet)
router.register(r'activity', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
