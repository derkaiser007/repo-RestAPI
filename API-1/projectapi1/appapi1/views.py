from django.http import HttpResponse

from rest_framework import viewsets, mixins, generics

from .models import CatResult
from .serializers import CatResultSerializer, TokenSerializer

from rest_framework import permissions
from .permissions import IsStaffEditorPermission

from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
def home(request):
    return HttpResponse("Hello World!")

# class CatResultViewSet(viewsets.ModelViewSet):
#     '''
#     get -> list -> Queryset
#     get -> retrieve -> Product Instance Detail View
#     post -> create -> New Instance
#     put -> Update
#     patch -> Partial UPdate
#     delete -> destroy 
#     '''
#     queryset = CatResult.objects.all()
#     serializer_class = CatResultSerializer
#     lookup_field = 'pk' # default

class CreateAPIView(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = CatResult.objects.all()
    serializer_class = CatResultSerializer
    lookup_field = 'pk' # default
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAPIView(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = CatResult.objects.all()
    serializer_class = CatResultSerializer
    lookup_field = 'pk' # default
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RetrieveAPIView(mixins.RetrieveModelMixin,
                      generics.GenericAPIView):
    queryset = CatResult.objects.all()
    serializer_class = CatResultSerializer
    lookup_field = 'pk' # default
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class DestroyAPIView(mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = CatResult.objects.all()
    serializer_class = CatResultSerializer
    lookup_field = 'pk' # default
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UpdateAPIView(mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    queryset = CatResult.objects.all()
    serializer_class = CatResultSerializer
    lookup_field = 'pk' # default
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class UserRegister(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = TokenSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token , _ = Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'payload': serializer.data, 'token': str(token)})



    

