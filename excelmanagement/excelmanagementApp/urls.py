from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from .views import HomeView, UploadFileView, FilterView, ViewView, LoginView, LogoutView, ExportCSVView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', UploadFileView.as_view(), name='upload'),
    path('filter/', FilterView.as_view(), name='filter'),
    path('view/', ViewView.as_view(), name="view"),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    path('download/', ExportCSVView.as_view(), name='download')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
