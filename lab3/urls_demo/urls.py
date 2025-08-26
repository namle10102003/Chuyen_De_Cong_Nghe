from django.urls import path, re_path, include, register_converter
from . import views
from . import page_patterns
from . import converters

# Register custom converter
register_converter(converters.FourDigitYearConverter, "yyyy")

extra_patterns = [
    path("reports/", views.report),
    path("reports/<int:id>/", views.report),
    path("charge/", views.charge),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('current-datetime/', views.current_datetime, name='current-datetime'),
    path('async-current-datetime/', views.async_current_datetime, name='async-current-datetime'),
    path('my-view/', views.my_view, name='my-view'),
    path('created/', views.created_view, name='created-view'),
    path('detail-404/<int:poll_id>/', views.detail_404, name='detail-404'),
    path('articles/2003/', views.special_case_2003, name='special-case-2003'),
    path('articles/<int:year>/', views.year_archive, name='year-archive'),
    path('articles/<int:year>/<int:month>/', views.month_archive, name='month-archive'),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail, name='article-detail'),
    re_path(r'^regex/(?P<word>\w{4,8})/$', views.regex_demo, name='regex-demo'),
    # Custom converter
    path('custom-year/<yyyy:year>/', views.year_archive, name='custom-year-archive'),
    # re_path with named groups
    re_path(r'^re-articles/(?P<year>[0-9]{4})/$', views.year_archive, name='re-year-archive'),
    re_path(r'^re-articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, name='re-month-archive'),
    re_path(r'^re-articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail, name='re-article-detail'),
    # include() with extra_patterns
    path('credit/', include((extra_patterns, 'credit'))),
    # include() with page_patterns
    path('<page_slug>-<page_id>/', include(page_patterns)),
    # Default argument for view
    path('blog/', views.page),
    path('blog/page<int:num>/', views.page),
    # Passing extra options to view
    path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}),

    # re_path with unnamed and nested groups
    re_path(r"^blog/(page-([0-9]+)/)?$", views.blog_articles),
    re_path(r"^comments/(?:page-(?P<page_number>[0-9]+)/)?$", views.comments),

    # include() as tuple with namespace (polls)
    path('polls/', include(([
        path('', views.index, name='index'),
        path('<int:pk>/', views.detail, name='detail'),
    ], 'polls'))),
]

# Error handler example (should be set in root URLconf)
handler404 = 'urls_demo.views.custom_404_view'
handler500 = 'urls_demo.views.my_custom_error_view'
handler403 = 'urls_demo.views.my_custom_permission_denied_view'
handler400 = 'urls_demo.views.my_custom_bad_request_view'