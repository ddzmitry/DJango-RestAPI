

from django.shortcuts import render
# import viewsets 
from rest_framework import viewsets
# import API view and respond 
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
# for login funcitonality
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
# for be able to update
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# import token
from rest_framework.authentication import TokenAuthentication
# to be able to see ontent only for authenicated usrs
from rest_framework.permissions import IsAuthenticated


# import serializer
from . import serializers
# Create your views here.
from . import models
# import premissions
from . import permissions
#  FOR SEARCH 
from rest_framework import filters


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
    # creating view set using ViewSet model
class HelloViewSet(viewsets.ViewSet):
    """Test API viewSet"""
    # for viewSets we use serializeClass
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """Return a Hello World message"""
        # creating viewset to display
        a_viewset = [
            'Uses actions (list,create,retrieve,update,partial_update)',
            'Automatically maps to URLs using Routes',
            'Provides mor funcitonality with less code.'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})
    
    def create(self,request):
        """Create a new hello message"""
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)

            return Response({"message":message})
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        """handles getting an object by tis ID."""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updated object"""
        return Response({'http_method':'Put'})

    def partial_update(self,request,pk=None):
        """Handles updating a part of an object,"""

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """handles Removing Object"""
        return Response({'http_method':'DELETE'})
        
        # createing viewset for user Model
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles Creating reading and updating models"""
    # set up serializer_class
    serializer_class = serializers.UserProfileSerializer
    # get all users
    queryset = models.UserProfile.objects.all()
    # adding token authenication 
    #  make sure to add commas because it makes is immutable so it can't be changed
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    # adding filter as tuples
    # This how it adds
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Check Email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer
    # create function
    def create(self,request):
        """Use the ObtainAuthToken APIView to validate and create token!"""
        # create login
        # will return token type 3d19f55acaccb093b9a382cf09ff9027b7a101cb
        return ObtainAuthToken().post(request)
# create user profile feed view

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handels Creating,reading and updating feed"""
    # add authenication
    authentication_classes = (TokenAuthentication,)
    # add serializer
    serializer_class = serializers.ProfileFeedItemSerializer
    # queryset we pull feeds from models
    queryset = models.ProfileFeed.objects.all()
    # permissions to allow to update or modify if they are logged in
    # 
    # permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)
    # and here to be able to see content ONLY for autenicated users
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)
    

    """Adding functionality to view"""
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)
