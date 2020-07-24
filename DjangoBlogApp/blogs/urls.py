from django.urls import path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
)

from .views import (
    BlogsTemplete, BlogView,
    BlogUploadView, AutherCreateView,BlogDeleteView,
    AutherUpdateView,BlogDetailsView,UpdateBlogView,
                    )

app_name = 'blogs'
urlpatterns=[
    path("login/",LoginView.as_view(template_name="blogs/login.html"),name="login"),
    path("logout/",LogoutView.as_view(next_page=reverse_lazy('blogs:login')),name="logout"),

    path('basepage/',BlogsTemplete.as_view(),name="basepage"),
    path("blogpage/",BlogView.as_view(),name="blogpage"),
    path("createauther/",AutherCreateView.as_view(),name="createauther"),
    path("autherupdate/", AutherUpdateView.as_view(), name="autherupdate"),

    path("createblog/",BlogUploadView.as_view()),
    path("deleteblog/<int:pk>",BlogDeleteView.as_view(),name="deleteblog"),
    path('blogdetails/',BlogDetailsView.as_view(),name="blogdetails"),
    path("blogupdate/",UpdateBlogView.as_view(),name="blogupdate")
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)