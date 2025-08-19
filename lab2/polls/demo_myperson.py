import os
import sys
import django

# Thêm đường dẫn dự án vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Person, MyPerson

# Tạo một đối tượng Person
p = Person.objects.create(first_name="foobar")
print('Person.objects.create:', p)

# Truy vấn MyPerson với first_name="foobar"
try:
    myp = MyPerson.objects.get(first_name="foobar")
    print('MyPerson.objects.get:', myp)
except MyPerson.DoesNotExist:
    print('Không tìm thấy MyPerson với first_name="foobar"')