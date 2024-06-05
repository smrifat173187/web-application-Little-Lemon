from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework.parsers import JSONParser
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer

@require_http_methods(["GET"])
def get_menu(request):
    menu_items = MenuItem.objects.all()
    serializer = MenuItemSerializer(menu_items, many=True)
    return JsonResponse(serializer.data, safe=False)

@require_http_methods(["POST"])
def create_booking(request):
    data = JSONParser().parse(request)
    serializer = BookingSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)
