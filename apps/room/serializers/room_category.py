from rest_framework import serializers

from apps.room.models import RoomCategory


class RoomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = '__all__'


class RoomCategoryReadOnlySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fid = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    # services = serializers.ManyToManyField(
    #     Service,
    #     related_name="room_categorys",
    #     null=True,
    #     blank=True,
    # )
