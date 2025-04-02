from rest_framework import serializers
from .models import Task

class CreateTaskDto(serializers.Serializer):
    titulo = serializers.CharField(max_length=255)
    descricao = serializers.CharField(allow_blank=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)


class ListarTaskDto(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

