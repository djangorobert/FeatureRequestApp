from rest_framework import serializers
from .models import FeatureRequest

class FeatureRequestSerializer(serializers.HyperlinkedModelSerializer):
    target_date = serializers.DateTimeField()
    class Meta:
        model = FeatureRequest
        fields = ('title', 'description', 'client', 'priority', 'target_date', 'department')
