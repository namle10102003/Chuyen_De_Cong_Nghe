import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.db.models import F
from polls.models.blog_entry import Blog, Entry

def entry_blog_examples():
    # Đảm bảo có dữ liệu mẫu
    blog1, _ = Blog.objects.get_or_create(pk=1, defaults={"name": "Blog 1", "tagline": "Tagline 1"})
    blog2, _ = Blog.objects.get_or_create(pk=2, defaults={"name": "Blog 2", "tagline": "Tagline 2"})
    entry1, _ = Entry.objects.get_or_create(pk=1, defaults={"blog": blog1, "headline": "Entry 1", "body_text": "Text 1", "pub_date": "2005-01-01", "mod_date": "2005-01-01", "number_of_comments": 1, "number_of_pingbacks": 0, "rating": 5})
    entry2, _ = Entry.objects.get_or_create(pk=2, defaults={"blog": blog2, "headline": "Entry 2", "body_text": "Text 2", "pub_date": "2005-01-01", "mod_date": "2005-01-01", "number_of_comments": 2, "number_of_pingbacks": 1, "rating": 6})

    # So sánh
    some_entry = entry1
    other_entry = entry2
    print(some_entry == other_entry)
    print(some_entry.id == other_entry.id)
    some_obj = blog1
    other_obj = blog2
    print(some_obj == other_obj)
    print(some_obj.name == other_obj.name)

    # Xóa entry
    e = Entry.objects.get(pk=2)
    print(e.delete())
    # Xóa nhiều entry theo điều kiện
    print(Entry.objects.filter(pub_date__year=2005).delete())

    # Lấy Blog
    b = Blog.objects.get(pk=1)
    # Gán tất cả entry về blog này
    Entry.objects.update(blog=b)
    # Cập nhật headline cho tất cả entry thuộc blog này
    Entry.objects.filter(blog=b).update(headline="Everything is the same")
    # Tăng number_of_pingbacks lên 1 cho tất cả entry
    Entry.objects.update(number_of_pingbacks=F("number_of_pingbacks") + 1)
    # Không thực hiện update headline bằng F("blog__name") vì sẽ lỗi FieldError

    # Truy vấn liên kết Blog
    e = Entry.objects.get(id=1)
    print(e.blog)
    some_blog = Blog.objects.get(pk=1)
    e.blog = some_blog
    e.save()
    # Không gán e.blog = None vì trường blog không cho phép null
    print(e.blog)
    print(e.blog)
    e = Entry.objects.select_related().get(id=1)
    print(e.blog)
    print(e.blog)
    b = Blog.objects.get(id=1)
    print(b.entry_set.all())
    print(b.entry_set.filter(headline__contains="Lennon"))
    print(b.entry_set.count())
    # Nếu Blog có related_name='entries' trong ForeignKey
    # print(b.entries.all())
    # print(b.entries.filter(headline__contains="Lennon"))
    # print(b.entries.count())

if __name__ == "__main__":
    entry_blog_examples()
