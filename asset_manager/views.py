from rest_framework import generics
from .models import Project#, Asset, SubAsset
from .serializers import ProjectSerializer#, AssetSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# class AssetList(generics.ListCreateAPIView):
#     queryset = Asset
#     serializer_class = AssetSerializer