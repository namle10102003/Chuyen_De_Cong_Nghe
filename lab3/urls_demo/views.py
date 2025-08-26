
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
