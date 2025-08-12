import os
import django
import sys

# Thêm đường dẫn dự án vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Thiết lập biến môi trường Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Question
from django.utils import timezone

# Hiển thị tất cả các Question hiện có
print('Tất cả Question:', list(Question.objects.all()))

# Tạo một Question mới
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
print('ID mới:', q.id)

# Truy cập các trường của model
print('question_text:', q.question_text)
print('pub_date:', q.pub_date)

# Thay đổi giá trị và lưu lại
q.question_text = "What's up?"
q.save()
print('question_text mới:', q.question_text)

# Hiển thị lại tất cả các Question
print('Tất cả Question sau khi thêm:', list(Question.objects.all()))