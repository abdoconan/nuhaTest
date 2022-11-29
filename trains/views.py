from HelperClasses.GenericView import CRUDView


from trains import models
from trains import serializers

# Create your views here.


class TrainTypeView(CRUDView):
    base_model = models.TrainType
    base_serializer = serializers.TrainTypeSerializers


class CoachCompisitionView(CRUDView):
    base_model = models.CoachCompisition
    base_serializer = serializers.CoachCompisitionSerializers
