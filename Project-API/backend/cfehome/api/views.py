import json
from django.shortcuts import render

from django.http import JsonResponse, HttpResponse

from products.models import Product

from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

# Create your views here.
@api_view(["POST"])
def api_home(request, *args, **kwargs):

    #return JsonResponse({"message": "Django Api Response"})

    """body = request.body
    print(body)
    return JsonResponse({"message": "Django Api Response"})"""


    """body = request.body #byte string of Json Data
    data = {}
    try:
        data = json.loads(body) #byte string of Json Data -> Python Dict
    except:
        pass
    print(data)
    return JsonResponse({"message": "Django Api Response"})"""


    """body = request.body #byte string of Json Data
    data = {}
    try:
        data = json.loads(body) #byte string of Json Data -> Python Dict
    except:
        pass
    #data['headers'] = request.headers
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type #request.META
    print(data)
    return JsonResponse(data)"""

    """model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)"""


    """model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        #data = model_to_dict(model_data)
        data = model_to_dict(model_data, fields = ['id', 'title'])
    return JsonResponse(data)"""


    """model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
        print(data)
        #data = model_to_dict(model_data, fields = ['id', 'title'])
        json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers = {"content-type":"application/json"})"""

    #DRF API View
    """model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        #data = model_to_dict(model_data)
        data = model_to_dict(model_data, fields = ['id', 'title'])
    return Response(data)"""

    """instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(model_data)
        #data = model_to_dict(model_data, fields = ['id', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)"""

    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception = True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invalid": "invalid data"}, status = 400)

