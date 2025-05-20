from django.db import models

class Resume(models.Model):
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.TextField()
    soft_skills = models.TextField()
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)


    def __str__(self):
        return self.full_name

