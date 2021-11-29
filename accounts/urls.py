from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('registerExperience',views.registerExperience,name='add'),
    path('experiences',views.experiences,name='experiences'),
    path('single/<int:year>/', views.single,name='single'),
    path('editExperience',views.editExperience,name='edit'),
    path('deleteExperience',views.deleteExperience,name='delete'),
    path('search',views.search,name='search')
]
