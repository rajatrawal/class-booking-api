from django.shortcuts import render
from . models import FitnessClass,ClassBooking
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import ClassBookingSerializer,FitnessClassSerializer
# Create your views here.


class ClassBookingListView(APIView):
    def get(self,request):
        email = request.query_params.get('email')
        if not  email:
            return Response({'error':'Email is required'},status=HTTP_400_BAD_REQUEST)
        bookings = ClassBooking.objects.filter(client_email = email )
        serializer = ClassBookingSerializer(bookings,many=True)
        return Response(serializer.data,status=200)
    
class ClassBookingCreateView(APIView):
    def post(self,request):
        serializer = ClassBookingSerializer(data =request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"data":serializer.data},status=201)
        
        return Response(serializer.errors,status=400)



class FitnessClassListCreateView(APIView):
    def get(self,request):
        fitness_classes = FitnessClass.objects.all().order_by('datetime')
        serializer = FitnessClassSerializer(fitness_classes,many=True)
        return Response(serializer.data,status=200)
    
    def post(self,request):
        serializer = FitnessClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Fitness Class Created Sucessfully',"data":serializer.data},status=201)
        return Response(serializer.errors,status=400)
        