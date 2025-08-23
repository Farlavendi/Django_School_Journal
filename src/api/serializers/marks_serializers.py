from rest_framework import serializers

from api.models import Marks


class MarksSerializer(serializers.ModelSerializer):
    maths = serializers.CharField(allow_blank=True)
    english = serializers.CharField(allow_blank=True)
    physics = serializers.CharField(allow_blank=True)
    chemistry = serializers.CharField(allow_blank=True)
    history = serializers.CharField(allow_blank=True)
    geography = serializers.CharField(allow_blank=True)
    literature = serializers.CharField(allow_blank=True)

    class Meta:
        model = Marks
        fields = ("maths", "english", "physics", "chemistry", "history", "geography", "literature")