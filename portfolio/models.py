from django.db import models

# ---------------------------------------------
# Section: About
# ---------------------------------------------
class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Section"


# ---------------------------------------------
# Section: Skills
# ---------------------------------------------
class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    ]
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, choices=PROFICIENCY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.proficiency})"


# ---------------------------------------------
# Section: Certificates
# ---------------------------------------------
class Certificate(models.Model):
    title = models.CharField(max_length=255)
    issued_by = models.CharField(max_length=255)
    date_issued = models.DateField()
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.issued_by}"


# ---------------------------------------------
# Section: Projects
# ---------------------------------------------
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    technologies_used = models.CharField(max_length=255)
    project_link = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


# ---------------------------------------------
# Section: Experience
# ---------------------------------------------
class Experience(models.Model):
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.role} at {self.company}"


# ---------------------------------------------
# Section: Education
# ---------------------------------------------
class Education(models.Model):
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"


# ---------------------------------------------
# Section: Learning (Ongoing Skills / Courses)
# ---------------------------------------------
class Learning(models.Model):
    STATUS_CHOICES = [
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ]

    topic = models.CharField(max_length=255)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.topic} ({self.status})"


# ---------------------------------------------
# Section: Activities (Posts, Contributions, etc.)
# ---------------------------------------------
class Activity(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='activities/', blank=True, null=True)

    def __str__(self):
        return self.title
