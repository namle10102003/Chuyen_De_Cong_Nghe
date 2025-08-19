import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models.blog_entry import Blog, Entry, Author

# Tạo Blog mới
b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
b.save()

# Đổi tên Blog có pk=5 thành "New name" nếu tồn tại
try:
    b5 = Blog.objects.get(pk=5)
    b5.name = "New name"
    b5.save()
except Blog.DoesNotExist:
    print("Blog với pk=5 không tồn tại.")

# Lấy entry có pk=1
try:
    entry = Entry.objects.get(pk=1)
    cheese_blog = Blog.objects.get(name="Cheddar Talk")
    entry.blog = cheese_blog
    entry.save()
except Entry.DoesNotExist:
    print("Entry với pk=1 không tồn tại.")
except Blog.DoesNotExist:
    print("Blog với tên 'Cheddar Talk' không tồn tại.")

# Tạo Author Joe và thêm vào entry
try:
    joe = Author.objects.create(name="Joe")
    entry.authors.add(joe)
except Exception as e:
    print(f"Lỗi khi thêm Joe: {e}")

# Tạo các Author khác và thêm vào entry
try:
    john = Author.objects.create(name="John")
    paul = Author.objects.create(name="Paul")
    george = Author.objects.create(name="George")
    ringo = Author.objects.create(name="Ringo")
    entry.authors.add(john, paul, george, ringo)
except Exception as e:
    print(f"Lỗi khi thêm các tác giả khác: {e}")