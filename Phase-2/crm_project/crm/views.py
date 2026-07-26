from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth import authenticate, login
from .models import Contact, Interaction
from .serializers import UserSerializer, ContactSerializer, InteractionSerializer

# --- 1. REGISTER ROUTE ---
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully!", "user_id": user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- 2. LOGIN ROUTE ---
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful!", "user_id": user.id}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# --- 3. CONTACTS LIST/CREATE (WITH THE "GUARD") ---
class ContactListCreateView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # GUARD: ONLY return contacts belonging to the logged-in user
        return Contact.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # GUARD: Automatically assign the new contact to the logged-in user
        serializer.save(user=self.request.user)

# --- 4. CONTACT DETAIL/UPDATE/DELETE (WITH THE "GUARD") ---
class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # GUARD: Only allow access to contacts belonging to this user
        return Contact.objects.filter(user=self.request.user)