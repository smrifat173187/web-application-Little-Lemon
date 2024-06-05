from django.test import RequestFactory, TestCase
from .views import get_menu, create_booking
from .models import MenuItem, Booking

class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.menu_item = MenuItem.objects.create(name='Test Item', price=10.99)
        self.booking = Booking.objects.create(name='Test Booking', date='2023-03-01', time='12:00')

    def test_get_menu(self):
        request = self.factory.get('/menu/')
        response = get_menu(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_booking(self):
        data = {'name': 'Test Booking', 'date': '2023-03-01', 'time': '12:00'}
        request = self.factory.post('/bookings/', data, content_type='application/json')
        response = create_booking(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 2)
