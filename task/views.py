from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import CreateTaskDto, ListarTaskDto

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = ListarTaskDto

    def create(self, request):
        serializer = CreateTaskDto(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Tarefa cadastrada com sucesso", status=status.HTTP_201_CREATED)
        return Response("Erro, tente novamente mais tarde", status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        tarefas = Task.objects.all()
        serializer = ListarTaskDto(tarefas, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response("Tarefa não localizada",status=status.HTTP_404_NOT_FOUND)
        serializer = ListarTaskDto(task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response("Tarefa não localizada", status=status.HTTP_404_NOT_FOUND)
        serializer = ListarTaskDto(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Atualizada com sucesso", status=status.HTTP_200_OK)
        return Response("Comando inválido, por favor tente outro comando", status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response("Tarefa não localizada", status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Atualizada com sucesso", status=status.HTTP_200_OK)
        return Response("comando inválido", status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response("Deletada com sucesso",status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response("Tarefa não encontrada",status=status.HTTP_404_NOT_FOUND)

