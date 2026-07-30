from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from .models import Contact, Interaction
from .serializers import (
    UserSerializer, ContactSerializer, InteractionSerializer,
    LoginSerializer, DraftRequestSerializer
)
from .services.ai_service import generate_followup_draft

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful!", "user_id": user.id})
        return Response({"error": "Invalid credentials"}, status=401)

class ContactListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

class GenerateDraftView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DraftRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact_id = serializer.validated_data['contact_id']
        try:
            contact = Contact.objects.get(id=contact_id, user=request.user)
            interactions = Interaction.objects.filter(contact=contact).order_by('-interaction_date')
            notes_history = [i.notes for i in interactions if i.notes]
            draft = generate_followup_draft(contact.name, notes_history)
            return Response({
                "contact_id": contact.id,
                "contact_name": contact.name,
                "draft": draft,
                "interactions_count": len(notes_history)
            })
        except Contact.DoesNotExist:
            return Response({"error": "Contact not found"}, status=404)