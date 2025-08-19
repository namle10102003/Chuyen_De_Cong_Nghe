import os
import sys
import django

# Thêm đường dẫn dự án vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Place, Restaurant

# Truy vấn Place có tên "Bob's Cafe"
places = Place.objects.filter(name="Bob's Cafe")
print('Place.objects.filter(name="Bob\'s Cafe"):', list(places))

# Truy vấn Restaurant có tên "Bob's Cafe"
restaurants = Restaurant.objects.filter(name="Bob's Cafe")
print('Restaurant.objects.filter(name="Bob\'s Cafe"):', list(restaurants))

# Lấy Place với id=12
try:
    p = Place.objects.get(id=12)
    print('Place.objects.get(id=12):', p)
    # Nếu p là Restaurant, truy xuất child class
    if hasattr(p, 'restaurant'):
        print('p.restaurant:', p.restaurant)
    else:
        print('p không phải là Restaurant')
except Place.DoesNotExist:
    print('Không tìm thấy Place với id=12')
