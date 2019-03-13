from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset allows us to create a full CRUD api without specifying explicit methods for its functionality, specify an endpoint to make get/post requests
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all() #will get all the leads
    permission_classes = [
        permissions.AllowAny #change this to only allow you access to your own leads, but for now its open
    ]
    serializer_class = LeadSerializer

