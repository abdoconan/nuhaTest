from rest_framework import serializers

from trains.models import TrainType


class TrainTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = TrainType
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
