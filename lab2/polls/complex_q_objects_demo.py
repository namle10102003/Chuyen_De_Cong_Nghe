
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from polls.models import Poll

from datetime import date

# Tạo dữ liệu mẫu cho Poll
def create_sample_polls():
    Poll.objects.all().delete()
    Poll.objects.create(question="What is your name?", pub_date=date(2005, 5, 2))
    Poll.objects.create(question="Who are you?", pub_date=date(2005, 5, 2))
    Poll.objects.create(question="What do you do?", pub_date=date(2005, 5, 6))
    Poll.objects.create(question="Where are you from?", pub_date=date(2006, 1, 1))
    Poll.objects.create(question="Why study Django?", pub_date=date(2005, 5, 6))
    Poll.objects.create(question="How old are you?", pub_date=date(2007, 8, 19))

create_sample_polls()

"""
Demo về sử dụng Q objects trong Django ORM để thực hiện các truy vấn phức tạp (AND, OR, NOT).
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from django.db.models import Q
from datetime import date
from polls.models import Poll

def demo_complex_q_objects():
    # Q object đơn giản
    q1 = Q(question__startswith="What")
    q2 = Q(question__startswith="Who")
    q3 = Q(pub_date__year=2005)

    # Kết hợp Q object với toán tử | (OR)
    or_query = Q(question__startswith="Who") | Q(question__startswith="What")
    polls_or = Poll.objects.filter(or_query)

    # Kết hợp Q object với toán tử ~ (NOT)
    not_query = Q(question__startswith="Who") | ~Q(pub_date__year=2005)
    polls_not = Poll.objects.filter(not_query)

    # Truy vấn với nhiều Q object (AND)
    polls_and = Poll.objects.get(
        Q(question__startswith="Who"),
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
    )

    # Truy vấn kết hợp Q object và keyword arguments
    polls_mix = Poll.objects.get(
        Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
        question__startswith="Who",
    )

    # Truy vấn không hợp lệ (Q object phải đứng trước keyword arguments)
    # Poll.objects.get(
    #     question__startswith="Who",
    #     Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
    # )

    print("Kết quả truy vấn OR:", polls_or)
    print("Kết quả truy vấn NOT:", polls_not)
    print("Kết quả truy vấn AND:", polls_and)
    print("Kết quả truy vấn kết hợp:", polls_mix)

if __name__ == "__main__":
    demo_complex_q_objects()
