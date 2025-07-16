from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from Blog.Blog import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogapp.urls'))
    
]
from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:id>/edit/',views.post_edit,name='post_edit'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete')

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)