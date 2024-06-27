# coffee_app/serializers.py
from rest_framework import serializers
from .models import Coffee, CoffeeImageModel


class CoffeeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeImageModel
        fields = ['coffee', 'image']

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:  # 2 MB limit
            raise serializers.ValidationError("Image size should not exceed 2 MB.")
        if not value.name.endswith(('.png', '.jpg', '.jpeg')):
            raise serializers.ValidationError("Only .png, .jpg and .jpeg files are allowed.")
        return value


class CoffeeSerializer(serializers.ModelSerializer):
    images = CoffeeImageSerializer(many=True, read_only=True)

    class Meta:
        model = Coffee
        fields = ['name', 'description', 'price', 'stock', 'is_available', 'images']
        

