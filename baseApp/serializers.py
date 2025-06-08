from rest_framework import serializers
from .models import ClassBooking, FitnessClass


class ClassBookingSerializer(serializers.ModelSerializer):
    class_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ClassBooking
        fields = ['id',  'client_name', 'class_id',
                  'client_email', 'booking_datetime', 'phone_number']

    def validate(self, data):
        try:
            fitness_class = FitnessClass.objects.get(id=data['class_id'])
        except FitnessClass.DoesNotExist:
            raise serializers.ValidationError('Invalid Class ID ')

        if fitness_class.total_slots <= 0:
            raise serializers.ValidationError('Slot are not available')

        data['fitness_class'] = fitness_class
        return data

    def create(self, validated_data):
        validated_data.pop('class_id')
        fitness_class = validated_data.pop('fitness_class')
        fitness_class.available_slots = fitness_class.available_slots - 1
        fitness_class.save()
        return ClassBooking.objects.create(fitness_class=fitness_class, **validated_data)


class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'
