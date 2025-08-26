from rest_framework import serializers

from api.models import Marks


class MarksSerializer(serializers.ModelSerializer):
    maths = serializers.IntegerField(min_value=1, max_value=12, allow_null=True)
    english = serializers.IntegerField(min_value=1, max_value=12, allow_null=True)
    physics = serializers.IntegerField(min_value=1, max_value=12, allow_null=True)
    chemistry = serializers.IntegerField(min_value=1, max_value=12, allow_null=True)
    history = serializers.IntegerField(min_value=1, max_value=12, allow_null=True)
    geography = serializers.IntegerField(min_value=1, max_value=12, allow_null=True)
    literature = serializers.IntegerField(min_value=1, max_value=12, allow_null=True)

    class Meta:
        model = Marks
        fields = (
            "student", "maths", "english", "physics", "chemistry", "history",
            "geography", "literature",
        )
