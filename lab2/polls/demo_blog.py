import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models.blog_entry import Blog, Entry, Author
from datetime import date, timedelta
from django.db.models import F, Min, OuterRef, Subquery, Sum

def create_sample_data():
    # Xóa tất cả dữ liệu cũ
    Blog.objects.all().delete()
    Author.objects.all().delete()
    Entry.objects.all().delete()

    # Tạo Blog mẫu
    blog1 = Blog.objects.create(pk=1, name="Cheddar Talk", tagline="Cheese news.")
    blog2 = Blog.objects.create(pk=5, name="Beatles Blog", tagline="All the latest Beatles news.")

    # Tạo Author mẫu
    authors = [
        Author.objects.create(name="Joe", email="joe@example.com"),
        Author.objects.create(name="John", email="john@example.com"),
        Author.objects.create(name="Paul", email="paul@example.com"),
        Author.objects.create(name="George", email="george@example.com"),
        Author.objects.create(name="Ringo", email="ringo@example.com"),
    ]

    # Tạo 10 Entry mẫu
    for i in range(1, 11):
        entry = Entry.objects.create(
            pk=i,
            blog=blog1 if i % 2 == 1 else blog2,
            headline=f"Entry số {i}",
            body_text=f"Nội dung entry {i}",
            pub_date=date(2025, 8, 19),
            mod_date=date(2025, 8, 19),
            number_of_comments=i,
            number_of_pingbacks=i//2,
            rating=5+i
        )
        entry.authors.set(authors)

    return blog1, blog2

# --- Tạo dữ liệu ---
blog1, blog2 = create_sample_data()

# Đổi tên Blog pk=5 thành "New name"
try:
    b5 = Blog.objects.get(pk=5)
    b5.name = "New name"
    b5.save()
except Blog.DoesNotExist:
    print("Blog với pk=5 không tồn tại.")

# Lấy entry pk=1 và gán lại blog
try:
    entry = Entry.objects.get(pk=1)
    cheese_blog = Blog.objects.get(name="Cheddar Talk")
    entry.blog = cheese_blog
    entry.save()
except Entry.DoesNotExist:
    print("Entry với pk=1 không tồn tại.")
except Blog.DoesNotExist:
    print("Blog với tên 'Cheddar Talk' không tồn tại.")

# --- In dữ liệu rõ ràng ---
print("Danh sách Blog hiện có:", list(Blog.objects.all()))
print("Danh sách Entry hiện có:", [e.headline for e in Entry.objects.all()])

# Một vài kiểm tra queryset
queryset = Entry.objects.all()
print("Ngày xuất bản:", [e.pub_date for e in queryset])
print("Entry thứ 6:", queryset[5] if queryset.count() > 5 else "Không có")
print("Queryset rỗng?", bool(queryset))
print("Entry pk=1 có trong queryset?", Entry.objects.get(pk=1) in queryset)
print("Toàn bộ queryset:", list(queryset))