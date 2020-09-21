from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategory
from . import views
urlpatterns = [
    path('home/',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article'),
    path('add_post/', AddPostView.as_view(), name='addpost'),
    path('update_post/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path('article/<int:pk>/delete',DeletePostView.as_view(), name='deletepost'),
    path('add_category',AddCategory.as_view(), name='addcategory'),
    path('category/<str:cats>/',views.category_view, name='category'),
    path('like/<int:pk>',views.LikeView,name='like_post')
]