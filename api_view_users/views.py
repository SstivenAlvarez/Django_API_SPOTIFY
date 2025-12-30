from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Users
from .serializer import UsersSerializer

class UsersView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    # GET /api/usuarios/1/editar/
    @action(detail=True, methods=['get', 'put'], url_path='editar')
    def editar(self, request, pk=None):
        usuario = self.get_object()
        if request.method == 'GET':
            ser = UsersSerializer(usuario)
            return Response(ser.data)
        ser = UsersSerializer(usuario, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"ok": True, "user": ser.data})
        return Response({"error": ser.errors})

    # DELETE /api/usuarios/1/borrar/
    @action(detail=True, methods=['delete'], url_path='borrar')
    def borrar(self, request, pk=None):
        usuario = self.get_object()
        usuario.delete()
        return Response({"ok": True, "msg": "Usuario eliminado"})
