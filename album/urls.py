from . import views
from django.urls import path
from .views import deactivate_account, delete_account, profile

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("category_list/<str:category>/", views.CategoryList.as_view(), name="category"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
    path('templates/account/profile/', profile, name='profile'),  # Import the profile view
    path('account/deactivate/', deactivate_account, name='deactivate_account'),
    path('account/delete/', delete_account, name='delete_account'),
]
