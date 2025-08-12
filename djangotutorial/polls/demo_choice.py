import os
import django
import sys

# Thêm đường dẫn dự án vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Thiết lập biến môi trường Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Question, Choice
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

print('Tất cả Question:', list(Question.objects.all()))

# Lọc theo id
print('Lọc theo id=1:', list(Question.objects.filter(id=1)))
# Lọc theo question_text bắt đầu bằng "What"
print('Lọc question_text__startswith="What":', list(Question.objects.filter(question_text__startswith="What")))


# Lấy các câu hỏi được đăng năm nay
current_year = timezone.now().year
qs_this_year = Question.objects.filter(pub_date__year=current_year)
if qs_this_year:
    print('Các Question năm nay:', list(qs_this_year))
else:
    print('Không có Question nào năm nay')

# Thử lấy id không tồn tại
try:
    Question.objects.get(id=2)
except ObjectDoesNotExist:
    print('Không có Question với id=2')

# Lấy bằng pk
try:
    q = Question.objects.get(pk=1)
    print('Lấy bằng pk=1:', q)
    print('was_published_recently:', q.was_published_recently())
except ObjectDoesNotExist:
    print('Không có Question với pk=1')

# Thêm Choice cho Question pk=1
if 'q' in locals():
    print('Các choice hiện có:', list(q.choice_set.all()))
    q.choice_set.create(choice_text="Not much", votes=0)
    q.choice_set.create(choice_text="The sky", votes=0)
    c = q.choice_set.create(choice_text="Just hacking again", votes=0)
    print('Choice mới tạo:', c)
    print('Choice liên kết với Question:', c.question)
    print('Tất cả choice:', list(q.choice_set.all()))
    print('Số lượng choice:', q.choice_set.count())
    # Lọc Choice theo năm
    print('Choice theo năm:', list(Choice.objects.filter(question__pub_date__year=current_year)))
    # Xóa choice bắt đầu bằng "Just hacking"
    c_del = q.choice_set.filter(choice_text__startswith="Just hacking")
    c_del.delete()
    print('Choice sau khi xóa:', list(q.choice_set.all()))