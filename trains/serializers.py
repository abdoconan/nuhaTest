from rest_framework import serializers

from trains.models import TrainType, CoachCompisition


class TrainTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = TrainType
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class CoachCompisitionSerializers(serializers.ModelSerializer):

    class Meta:
        model = CoachCompisition
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
