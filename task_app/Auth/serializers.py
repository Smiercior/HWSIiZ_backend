# users/serializers.py
from rest_framework.serializers import ModelSerializer
from .models import User
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class UserSerializer(RegisterSerializer):#ModelSerializer
    BHPCourse = serializers.BooleanField(
        required=False,
    )

    Abilities = serializers.CharField(
        required=False,
        max_length=64,
    )
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['Abilities'] = self.validated_data.get('Abilities', '')
        data_dict['BHPCourse'] = self.validated_data.get('BHPCourse', '')
        return data_dict


    # class Meta:
    #     model = User
    #     fields = ('BHPCourse', 'Abilities', 'email', 'last_login', 'date_joined', 'is_staff')