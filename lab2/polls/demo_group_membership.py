import os
import sys
import django
from datetime import date

# Thêm đường dẫn dự án vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Person, Group, Membership

# Tạo các đối tượng Person
ringo = Person.objects.create(name="Ringo Starr")
paul = Person.objects.create(name="Paul McCartney")

# Tạo Group
beatles = Group.objects.create(name="The Beatles")

# Tạo Membership cho Ringo
m1 = Membership(
    person=ringo,
    group=beatles,
    date_joined=date(1962, 8, 16),
    invite_reason="Needed a new drummer."
)
m1.save()
print('beatles.members.all():', list(beatles.members.all()))
print('ringo.group_set.all():', list(ringo.group_set.all()))

# Tạo Membership cho Paul
m2 = Membership.objects.create(
    person=paul,
    group=beatles,
    date_joined=date(1960, 8, 1),
    invite_reason="Wanted to form a band."
)
print('beatles.members.all():', list(beatles.members.all()))

# Thêm các thành viên khác
from polls.models import Person
john = Person.objects.create(name="John Lennon")
george = beatles.members.create(
    name="George Harrison", through_defaults={"date_joined": date(1960, 8, 1)}
)
beatles.members.add(john, through_defaults={"date_joined": date(1960, 8, 1)})
beatles.members.set([john, paul, ringo, george], through_defaults={"date_joined": date(1960, 8, 1)})


# Membership mới cho Ringo, kiểm tra trước khi tạo
if not Membership.objects.filter(person=ringo, group=beatles).exists():
    Membership.objects.create(
        person=ringo,
        group=beatles,
        date_joined=date(1968, 9, 4),
        invite_reason="You've been gone for a month and we miss you."
    )
else:
    print("Membership này đã tồn tại, không tạo mới.")
print('beatles.members.all():', list(beatles.members.all()))

# Xóa các Membership của Ringo
beatles.members.remove(ringo)
print('beatles.members.all():', list(beatles.members.all()))

# Beatles tan rã
beatles.members.clear()
print('Membership.objects.all():', list(Membership.objects.all()))

# Tìm các nhóm có thành viên tên bắt đầu bằng 'Paul'
groups_with_paul = Group.objects.filter(members__name__startswith="Paul")
print('Group có thành viên Paul:', list(groups_with_paul))

# Tìm các thành viên của Beatles gia nhập sau 1/1/1961
members_after_1961 = Person.objects.filter(
    group__name="The Beatles", membership__date_joined__gt=date(1961, 1, 1)
)
print('Thành viên Beatles sau 1/1/1961:', list(members_after_1961))


# Truy vấn Membership của Ringo, kiểm tra ngoại lệ
try:
    ringos_membership = Membership.objects.get(group=beatles, person=ringo)
    print('ringos_membership.date_joined:', ringos_membership.date_joined)
    print('ringos_membership.invite_reason:', ringos_membership.invite_reason)
except Membership.DoesNotExist:
    print('Không tìm thấy Membership của Ringo trong Beatles.')

try:
    ringos_membership2 = ringo.membership_set.get(group=beatles)
    print('ringos_membership2.date_joined:', ringos_membership2.date_joined)
    print('ringos_membership2.invite_reason:', ringos_membership2.invite_reason)
except Membership.DoesNotExist:
    print('Không tìm thấy Membership của Ringo trong Beatles (membership_set).')