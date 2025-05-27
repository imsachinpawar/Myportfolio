from rest_framework import serializers
from .models import About, Skill, Certificate, Project, Experience, Education, Learning, Activity

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'content']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency']

class CertificateSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = '__all__'  # or list explicitly
        read_only_fields = ['image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'technologies_used', 'project_link', 'start_date', 'end_date']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'role', 'company', 'description', 'start_date', 'end_date', 'location']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'degree', 'institution', 'start_year', 'end_year', 'description']

class LearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learning
        fields = ['id', 'topic', 'status', 'description']

class ActivitySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['image_url']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None
