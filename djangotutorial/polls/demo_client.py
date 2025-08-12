import os
import sys
import django

# Thêm đường dẫn dự án vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Thiết lập biến môi trường Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.test.utils import setup_test_environment
from django.test import Client
from django.urls import reverse

# Thiết lập môi trường test
setup_test_environment()

# Tạo client
client = Client()

# Gửi request tới '/'
response = client.get("/")
print('GET / status_code:', response.status_code)

# Gửi request tới '/polls/' bằng reverse
response = client.get(reverse("polls:index"))
print('GET /polls/ status_code:', response.status_code)
print('Nội dung response:', response.content)

# Lấy context latest_question_list nếu có
if hasattr(response, 'context') and response.context and "latest_question_list" in response.context:
    print('latest_question_list:', list(response.context["latest_question_list"]))
else:
    print('Không có context hoặc latest_question_list')
