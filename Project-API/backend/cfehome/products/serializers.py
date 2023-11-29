from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators

class ProductSerializer(serializers.ModelSerializer):
    terms_conditions = serializers.SerializerMethodField(read_only=True)
    #url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    #title = serializers.CharField(validators = [validators.validate_title])
    title = serializers.CharField(validators = [validators.unique_product_title, validators.validate_title_no_hello])
    name = serializers.CharField(source = 'title', read_only = True)
    class Meta:
        model = Product
        fields = [
            #'user',
            'pk',
            'url',
            'title',
            'name',
            'content',
            'price',
            'sale_price',
            #'sale_policy'
            'terms_conditions',
            'email'
        ]

    def get_terms_conditions(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.sale_policy()
    
    
    # def get_url(self, obj):
    #     return f"/api/products/{obj.pk}/" 
    
    
    # def get_url(self, obj):
    #     request = self.context.get('request') # self.request
    #     if request is None:
    #         return None
    #     return reverse("product-detail", kwargs = {"pk": obj.pk}, request = request) 
    #     #return reverse("product-edit", kwargs = {"pk": obj.pk}, request = request)
    

    def create(self, validated_data):
        email = validated_data.pop('email')
        obj = super().create(validated_data)
        #obj = Product.objects.create(**validated_data)
        print(email, obj)
        return obj
    
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().create(validated_data)
    

    
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a title name.")
    #     return value
    
    
    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user = user, title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a title name.")
    #     return value
    