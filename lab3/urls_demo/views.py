import datetime
import asyncio
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.template.loader import render_to_string, get_template, select_template
from django.views.generic import TemplateView
from django.views import View

# View render template với context mẫu
def template_demo(request):
	context = {
		'first_name': 'John',
		'last_name': 'Doe',
		'info': {'email': 'john@example.com'},
		'user': type('User', (), {'username': 'johndoe'})(),
		'fruits': ['Apple', 'Banana', 'Cherry'],
		'text': 'the web framework for perfectionists with deadlines',
		'is_active': True,
		'explain': [
			'Ví dụ này minh họa cách truyền context vào template Django.',
			'Template sử dụng biến, filter, tag for, if, comment.',
			'Bạn có thể mở rộng context để truyền thêm dữ liệu động.',
			'URL: /urls-demo/template-demo/'
		]
	}
	html = render(request, 'demo_template.html', context)
	# Thêm phần giải thích phía trên
	explain_html = '<h3>Giải thích:</h3><ul>' + ''.join(f'<li>{e}</li>' for e in context['explain']) + '</ul>'
	return HttpResponse(explain_html + html.content.decode())

# View dùng render_to_string
def template_string_demo(request):
	context = {
		'first_name': 'Jane',
		'last_name': 'Smith',
		'info': {'email': 'jane@example.com'},
		'user': type('User', (), {'username': 'janesmith'})(),
		'fruits': ['Orange', 'Mango'],
		'text': 'django template string demo',
		'is_active': False,
		'explain': [
			'Ví dụ này sử dụng render_to_string để render template ra chuỗi.',
			'Bạn có thể dùng kết quả này để gửi email, trả về API, hoặc nhúng vào response.',
			'URL: /urls-demo/template-string-demo/'
		]
	}
	html = render_to_string('demo_template.html', context)
	explain_html = '<h3>Giải thích:</h3><ul>' + ''.join(f'<li>{e}</li>' for e in context['explain']) + '</ul>'
	return HttpResponse(explain_html + html)

# View dùng select_template
def select_template_demo(request):
	context = {
		'first_name': 'Alice',
		'last_name': 'Nguyen',
		'info': {'email': 'alice@example.com'},
		'user': type('User', (), {'username': 'aliceng'})(),
		'fruits': ['Kiwi', 'Lemon'],
		'text': 'select template demo',
		'is_active': True,
		'explain': [
			'Ví dụ này sử dụng select_template để chọn template đầu tiên tồn tại trong danh sách.',
			'Thường dùng khi muốn cho phép override template theo app, theme, hoặc user.',
			'Nếu not_exist.html không tồn tại, sẽ dùng demo_template.html.',
			'URL: /urls-demo/select-template-demo/'
		]
	}
	template = select_template(['not_exist.html', 'demo_template.html'])
	html = template.render(context, request)
	explain_html = '<h3>Giải thích:</h3><ul>' + ''.join(f'<li>{e}</li>' for e in context['explain']) + '</ul>'
	return HttpResponse(explain_html + html)

# TemplateView trực tiếp trong URLconf
class AboutTemplateView(TemplateView):
	template_name = "about.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['extra'] = "Đây là TemplateView sử dụng trực tiếp trong URLconf. Bạn có thể truyền context vào template nếu muốn."
		context['note'] = "TemplateView rất phù hợp cho các trang tĩnh hoặc chỉ cần truyền ít dữ liệu."
		return context

# Subclass TemplateView
class AboutView(TemplateView):
	template_name = "about.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['extra'] = "Đây là AboutView kế thừa TemplateView, bạn có thể mở rộng logic, truyền thêm context, v.v."
		context['note'] = "Bạn có thể override get_context_data để truyền nhiều dữ liệu động vào template."
		return context

# Async class-based view
class AsyncView(View):
	async def get(self, request, *args, **kwargs):
		await asyncio.sleep(1)
		html = """
			<h2>Hello async world!</h2>
			<ul>
				<li>Đây là ví dụ async class-based view.</li>
				<li>View này sử dụng async def để xử lý bất đồng bộ.</li>
				<li>Thường dùng cho các tác vụ IO-bound như gọi API, truy vấn DB async, ...</li>
				<li>URL: /urls-demo/async-cbv/</li>
			</ul>
		"""
		return HttpResponse(html)

# Giả lập BookListView (không cần model thực)
class BookListView(View):
	def get(self, request, *args, **kwargs):
		books = [
			{"title": "Book 1", "publication_date": datetime.datetime(2023, 1, 1, 10, 0)},
			{"title": "Book 2", "publication_date": datetime.datetime(2024, 5, 20, 15, 30)},
		]
		last_book = max(books, key=lambda b: b["publication_date"])
		html = f"""
			<h2>Book List (Class-based View)</h2>
			<ul>
				<li>Danh sách sách (giả lập):</li>
				{''.join(f'<li>{b['title']} - {b['publication_date']}</li>' for b in books)}
				<li>Last Modified: {last_book['publication_date'].strftime('%a, %d %b %Y %H:%M:%S GMT')}</li>
				<li>GET sẽ trả về danh sách sách, HEAD chỉ trả về header Last-Modified.</li>
				<li>URL: /urls-demo/books/</li>
				<li>Đây là ví dụ CBV với cả GET và HEAD.</li>
			</ul>
		"""
		return HttpResponse(html)

	def head(self, request, *args, **kwargs):
		books = [
			{"title": "Book 1", "publication_date": datetime.datetime(2023, 1, 1, 10, 0)},
			{"title": "Book 2", "publication_date": datetime.datetime(2024, 5, 20, 15, 30)},
		]
		last_book = max(books, key=lambda b: b["publication_date"])
		response = HttpResponse(
			headers={
				"Last-Modified": last_book["publication_date"].strftime("%a, %d %b %Y %H:%M:%S GMT")
			},
		)
		return response

# A simple view trả về thời gian hiện tại
def current_datetime(request):
	now = datetime.datetime.now()
	html = f'''
		<h2>Current Datetime</h2>
		<ul>
			<li>Thời gian hiện tại: {now}</li>
			<li>View: current_datetime</li>
			<li>URL: /urls-demo/current-datetime/</li>
			<li>Đây là ví dụ view trả về thời gian hiện tại.</li>
		</ul>
	'''
	return HttpResponse(html)

# View trả về 404 hoặc 200
def my_view(request):
	foo = request.GET.get('foo', None)
	if foo:
		return HttpResponseNotFound("""
			<h2>Page not found (404)</h2>
			<ul>
				<li>Tham số foo: {foo}</li>
				<li>Trả về HttpResponseNotFound</li>
				<li>URL: /urls-demo/my-view/?foo=1</li>
			</ul>
		""")
	else:
		return HttpResponse("""
			<h2>Page was found (200)</h2>
			<ul>
				<li>Không có tham số foo</li>
				<li>Trả về HttpResponse 200</li>
				<li>URL: /urls-demo/my-view/</li>
			</ul>
		""")

# View trả về status code bất kỳ
def created_view(request):
	return HttpResponse("""
		<h2>Created (201)</h2>
		<ul>
			<li>Trả về status code 201 (Created)</li>
			<li>URL: /urls-demo/created/</li>
			<li>Ví dụ trả về mã HTTP bất kỳ</li>
		</ul>
	""", status=201)

# View raise Http404
def detail_404(request, poll_id):
	# Giả lập không tìm thấy poll
	raise Http404(f"Poll {poll_id} does not exist (ví dụ raise Http404)")

# Custom error handlers
	return HttpResponse("""
		<h2>Custom 404 page from mysite.views</h2>
		<ul>
			<li>Đây là trang 404 do bạn tự định nghĩa.</li>
			<li>URL không tồn tại hoặc bị lỗi.</li>
		</ul>
	""", status=404)

	return HttpResponse("""
		<h2>Custom 500 page from mysite.views</h2>
		<ul>
			<li>Đây là trang 500 do bạn tự định nghĩa.</li>
			<li>Lỗi server nội bộ.</li>
		</ul>
	""", status=500)

	return HttpResponse("""
		<h2>Custom 403 page from mysite.views</h2>
		<ul>
			<li>Bạn không có quyền truy cập tài nguyên này.</li>
			<li>Ví dụ custom handler403.</li>
		</ul>
	""", status=403)

	return HttpResponse("""
		<h2>Custom 400 page from mysite.views</h2>
		<ul>
			<li>Yêu cầu không hợp lệ.</li>
			<li>Ví dụ custom handler400.</li>
		</ul>
	""", status=400)

# Async view example
async def async_current_datetime(request):
	await asyncio.sleep(0.1)
	now = datetime.datetime.now()
	html = f'''
		<h2>Async Current Datetime</h2>
		<ul>
			<li>Thời gian hiện tại: {now}</li>
			<li>View: async_current_datetime (async)</li>
			<li>URL: /urls-demo/async-current-datetime/</li>
			<li>Ví dụ view async (Python async def)</li>
		</ul>
	'''
	return HttpResponse(html)

def index(request):
	return HttpResponse("""
		<h2>URL Dispatcher Demo - Index</h2>
		<ul>
			<li>Demo các loại URL pattern, converter, include, re_path, ...</li>
			<li>Thử các đường dẫn như /articles/2003/, /articles/2024/08/...</li>
			<li>Xem code trong urls_demo/urls.py và views.py</li>
		</ul>
	""")

def special_case_2003(request):
	return HttpResponse("""
		<h2>Special case: 2003</h2>
		<p>Đây là trang đặc biệt cho năm 2003.</p>
		<p>URL: /articles/2003/</p>
	""")

def year_archive(request, year, **kwargs):
	foo = kwargs.get('foo', None)
	return HttpResponse(f"""
		<h2>Year archive</h2>
		<ul>
			<li>Năm: {year}</li>
			<li>Tham số foo: {foo}</li>
			<li>URL: /articles/{year}/ hoặc /blog/&lt;int:year&gt;/</li>
		</ul>
	""")

def month_archive(request, year, month):
	return HttpResponse(f"""
		<h2>Month archive</h2>
		<ul>
			<li>Năm: {year}</li>
			<li>Tháng: {month}</li>
			<li>URL: /articles/{year}/{month}/</li>
		</ul>
	""")

def article_detail(request, year, month, slug):
	return HttpResponse(f"""
		<h2>Article detail</h2>
		<ul>
			<li>Năm: {year}</li>
			<li>Tháng: {month}</li>
			<li>Slug: {slug}</li>
			<li>URL: /articles/{year}/{month}/{slug}/</li>
		</ul>
	""")

def regex_demo(request, word):
	return HttpResponse(f"""
		<h2>Regex demo</h2>
		<ul>
			<li>Kết quả: {word}</li>
			<li>URL: /regex/&lt;word&gt;/ (4-8 ký tự)</li>
		</ul>
	""")

# Views for include() page_patterns example
def history(request, page_slug=None, page_id=None):
	return HttpResponse(f"""
		<h2>History</h2>
		<ul>
			<li>Page: {page_slug}-{page_id}</li>
			<li>URL: /&lt;page_slug&gt;-&lt;page_id&gt;/history/</li>
		</ul>
	""")

def edit(request, page_slug=None, page_id=None):
	return HttpResponse(f"""
		<h2>Edit</h2>
		<ul>
			<li>Page: {page_slug}-{page_id}</li>
			<li>URL: /&lt;page_slug&gt;-&lt;page_id&gt;/edit/</li>
		</ul>
	""")

def discuss(request, page_slug=None, page_id=None):
	return HttpResponse(f"""
		<h2>Discuss</h2>
		<ul>
			<li>Page: {page_slug}-{page_id}</li>
			<li>URL: /&lt;page_slug&gt;-&lt;page_id&gt;/discuss/</li>
		</ul>
	""")

def permissions(request, page_slug=None, page_id=None):
	return HttpResponse(f"""
		<h2>Permissions</h2>
		<ul>
			<li>Page: {page_slug}-{page_id}</li>
			<li>URL: /&lt;page_slug&gt;-&lt;page_id&gt;/permissions/</li>
		</ul>
	""")

# Views for extra_patterns (credit)
def report(request, id=None):
	return HttpResponse(f"""
		<h2>Credit report</h2>
		<ul>
			<li>ID: {id}</li>
			<li>URL: /credit/reports/ hoặc /credit/reports/&lt;id&gt;/</li>
		</ul>
	""")

def charge(request):
	return HttpResponse("""
		<h2>Credit charge</h2>
		<ul>
			<li>URL: /credit/charge/</li>
		</ul>
	""")

# View for default argument
def page(request, num=1):
	return HttpResponse(f"""
		<h2>Blog page</h2>
		<ul>
			<li>Trang: {num}</li>
			<li>URL: /blog/ hoặc /blog/page&lt;num&gt;/</li>
		</ul>
	""")

# re_path with unnamed/nested groups
def blog_articles(request, *args):
	return HttpResponse(f"""
		<h2>Blog articles (unnamed/nested group)</h2>
		<ul>
			<li>Args: {args}</li>
			<li>URL: /blog/(page-...)?</li>
		</ul>
	""")

def comments(request, page_number=None):
	return HttpResponse(f"""
		<h2>Comments (nested group)</h2>
		<ul>
			<li>Page number: {page_number}</li>
			<li>URL: /comments/(page-...)?</li>
		</ul>
	""")

# For include() as tuple with namespace
def detail(request, pk):
	return HttpResponse(f"""
		<h2>Polls detail</h2>
		<ul>
			<li>PK: {pk}</li>
			<li>URL: /polls/&lt;pk&gt;/</li>
		</ul>
	""")

# Custom 404 handler
def custom_404_view(request, exception):
	return HttpResponseNotFound("""
		<h2>Custom 404 page - Not Found</h2>
		<p>Trang bạn truy cập không tồn tại.</p>
		<ul>
			<li>Kiểm tra lại URL hoặc quay về <a href='/urls-demo/'>trang chính</a>.</li>
		</ul>
	""")
