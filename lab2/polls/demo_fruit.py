import os
import sys
import django

# Thêm đường dẫn dự án vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Fruit

# Tạo một đối tượng Fruit
fruit = Fruit.objects.create(name="Apple")
fruit.name = "Pear"
fruit.save()

# Lấy danh sách tên các loại fruit
names = list(Fruit.objects.values_list("name", flat=True))
print('Fruit names:', names)
