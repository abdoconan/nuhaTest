from HelperClasses.GenericView import CRUDView


from trains import models
from trains import serializers

# Create your views here.


class TrainTypeView(CRUDView):
    base_model = models.TrainType
    base_serializer = serializers.TrainTypeSerializers


class CoachCompisitionView(CRUDView):
    base_model = models.CoachCompoisition
    base_serializer = serializers.CoachCompisitionSerializers


class TrainCompoisitionView(CRUDView):
    base_model = models.TrainCompoisition
    base_serializer = serializers.TrainCompoisitionSerializers


class TrainCoachCompoisitionView(CRUDView):
    base_model = models.TrainCoachCompoisition
    base_serializer = serializers.TrainCoachCompoisitionSerializers


class TrainView(CRUDView):
    base_model = models.Train
    base_serializer = serializers.TrainSerializers
