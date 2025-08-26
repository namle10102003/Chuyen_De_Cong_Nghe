import datetime
from django.http import HttpResponse, HttpResponseNotFound, Http404

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
import asyncio
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

from django.http import HttpResponse

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
from django.http import HttpResponseNotFound
def custom_404_view(request, exception):
	return HttpResponseNotFound("""
		<h2>Custom 404 page - Not Found</h2>
		<p>Trang bạn truy cập không tồn tại.</p>
		<ul>
			<li>Kiểm tra lại URL hoặc quay về <a href='/urls-demo/'>trang chính</a>.</li>
		</ul>
	""")
