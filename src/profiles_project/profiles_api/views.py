from django.shortcuts import render
# import API view and respond 
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
# import serializer
from . import serializers
# Create your views here.



#  here we will create our views for API
class HelloApiView(APIView):
    """Test API View"""
    # address serializer
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of APIView features!"""

        an_apiview = [
            'Uses HTTP methods as functions(get,post,patch,out,delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
    def post(self,request):
        """ Create  a hello message with our name"""
        # we have to pass request to Serializer
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            # we can get name that was entered
            name = serializer.data.get("name")
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request, pk=None):
        """Patch request, only updates fields provided in the request"""
        # update differences 
        return Response({'method':'patch'})

    def put(self,request, pk=None):
        """Handels updating an object"""
        return Response({'method':'put'})
        

    def delete(self,request,pk=None):
        """Deletes the object"""

        return Response({'method':'delete'})
