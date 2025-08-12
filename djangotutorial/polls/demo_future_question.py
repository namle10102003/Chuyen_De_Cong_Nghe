import os
import sys
import django
import datetime
from django.utils import timezone

# Thêm đường dẫn dự án vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Thiết lập biến môi trường Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Question

# Tạo một Question với pub_date 30 ngày trong tương lai
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
print('pub_date:', future_question.pub_date)
print('was_published_recently:', future_question.was_published_recently())
