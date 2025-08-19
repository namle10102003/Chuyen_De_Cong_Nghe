import os
import sys
import django

# Thêm đường dẫn dự án vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Person

# Tạo một đối tượng Person
p = Person(name="Fred Flintstone", shirt_size="L")
p.save()
print('shirt_size:', p.shirt_size)
print('get_shirt_size_display:', p.get_shirt_size_display())