from . import views
from django.urls import path
from .views import profile, delete_profile


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('profile/', profile, name='users-profile'),
    path('delete-profile/', delete_profile, name='delete-profile'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("category_list/<str:category>/", views.CategoryList.as_view(), name="category"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
]
