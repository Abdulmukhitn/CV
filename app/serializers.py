from rest_framework import serializers

from app.models import Resume


class ResumeSerializer(serializers.Serializer):
    class Meta:
        model = Resume
        fields = ['full_name' , 'bio', 'skills']


