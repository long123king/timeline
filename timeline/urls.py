from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'timeline.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^frames/', include('frames.urls')),
]
