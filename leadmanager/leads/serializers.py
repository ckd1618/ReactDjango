from rest_framework import serializers
from leads.models import Lead

# Lead Serializer, you are creating a serializer from your Lead model
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
