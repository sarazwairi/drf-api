from django.db.models import fields
from rest_framework import serializers
from .models import Things

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title','purchaser','description')
        model=Things