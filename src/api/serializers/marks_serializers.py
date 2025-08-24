from rest_framework import serializers

from api.models import Marks


class MarksSerializer(serializers.ModelSerializer):
    maths = serializers.IntegerField(min_value=1, max_value=12, allow_blank=True)
    english = serializers.IntegerField(min_value=1, max_value=12, allow_blank=True)
    physics = serializers.IntegerField(min_value=1, max_value=12, allow_blank=True)
    chemistry = serializers.IntegerField(min_value=1, max_value=12, allow_blank=True)
    history = serializers.IntegerField(min_value=1, max_value=12, allow_blank=True)
    geography = serializers.IntegerField(min_value=1, max_value=12, allow_blank=True)
    literature = serializers.IntegerField(min_value=1, max_value=12, allow_blank=True)

    class Meta:
        model = Marks
        fields = (
            "student", "maths", "english", "physics", "chemistry", "history",
            "geography", "literature",
        )
