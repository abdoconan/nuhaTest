from rest_framework import serializers

from trains.models import TrainType, CoachCompoisition, TrainCompoisition, TrainCoachCompoisition, Train


class TrainTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = TrainType
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class CoachCompisitionSerializers(serializers.ModelSerializer):

    class Meta:
        model = CoachCompoisition
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class TrainCompoisitionSerializers(serializers.ModelSerializer):

    class Meta:
        model = TrainCompoisition
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class TrainCoachCompoisitionSerializers(serializers.ModelSerializer):

    class Meta:
        model = TrainCoachCompoisition
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class TrainSerializers(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
