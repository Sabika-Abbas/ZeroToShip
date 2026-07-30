from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Contact, Interaction

User = get_user_model()

# Serializer for User Registration
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'major', 'department']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            major=validated_data.get('major', ''),
            department=validated_data.get('department', '')
        )
        return user

# Serializer for Contacts (with the "Guard" built-in)
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'organization', 'role', 'email', 'linkedin_url', 'last_contacted_date']
        read_only_fields = ['user']

# Serializer for Interactions
class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['id', 'contact', 'interaction_date', 'type', 'notes']
        read_only_fields = ['contact']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class DraftRequestSerializer(serializers.Serializer):
    contact_id = serializers.IntegerField(help_text="ID of the contact to generate a draft for")