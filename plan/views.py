from rest_framework import viewsets
from .models import Plan
from .serializers import PlanSerializer
from .permissions import IsOwner

class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    permission_classes = [IsOwner]
