from rest_framework import serializers

from . import models
# creating serializer to test API
class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView."""


    name = serializers.CharField(max_length = 10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        # assign model
        model = models.UserProfile
        fields = ('id','email','name','password')
        # make passsword invisible
        extra_kwargs = {'password':{'write_only':True}}
        # this is how we will create a new user 
    def create(self,validated_data):
        """Create and return a new user"""
        # we are overriting model method
        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name'],

        )
        # and set password after being validated
        user.set_password(validated_data['password'])
        user.save()
        return user
# profile feed Serializer
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        # we specify wich model we are using for serializer
        model = models.ProfileFeed
        # provide fields that serializer is going to affect 
        fields = ('id', 'user_profile','status_text','created_on')
        # specify that only user that created the field can update it
        extra_kwargs = {'user_profile':{'read_only':True}}