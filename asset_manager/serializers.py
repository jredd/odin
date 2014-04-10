from rest_framework import serializers
from asset_manager.models import Project, Asset, SubAsset


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id',
                  'name',
                  'location',
                  'date',
        )


# class AssetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Asset
#         fields = ('id',
#                  'name',
#                  'created_by',
#                  'date',
#         )