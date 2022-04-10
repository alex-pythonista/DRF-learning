from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
from products.models import *
from products.serializers import ProductSerializer

# Create your views here.

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        # data = serializer.data
        return Response(serializer.data)



# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         # data = model_to_dict(model_data, fields=['id', 'title', 'sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)