"""lioninthecloset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from post.views import closet_view
from django.contrib import admin
from django.urls import path
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('closet/', views.closet_view, name="closet"),
    path('detail/<int:index>', views.item_detail, name="item_detail"),
    path('admin/', admin.site.urls),
    path('combination_detail/<int:index>', views.combination_detail, name="combination_detail"),
    path('login/', views.login_view, name = "login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="signup"),
    path('addtocombi/<int:index>/<int:pk>', views.add_to_combi, name="add_combi_item"),
    path('new/', views.new, name ="new"),
    path('create/', views.create, name ="create"),
    path('edit/<str:id>', views.edit, name ="edit"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
