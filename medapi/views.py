from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from main.forms import MedicineForm
from .serializers import MedicineSerializer
from main.models import Medicine
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_med(request):
    form = MedicineForm(request.POST)
    if form.is_valid():
        med = form.save()
        return Response({'id': med.id}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_med(request):
    med = Medicine.objects.all()
    serializer = MedicineSerializer(med, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_med(request, pk):
    med = get_object_or_404(Medicine, pk=pk)
    form = MedicineForm(request.data, instance=med)
    if form.is_valid():
        form.save()
        serializer = MedicineSerializer(med)
        return Response(serializer.data)
    else:
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_med(request, pk):
    try:
        med = Medicine.objects.get(pk=pk)
    except Medicine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    med.delete()
    return Response("deleted successfully")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_med(request):
    query = request.GET.get('query')
    med = Medicine.objects.filter(name__icontains=query)
    serializer = MedicineSerializer(med, many=True)
    return Response(serializer.data)