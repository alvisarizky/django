from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.IndexListView.as_view(), name="index"),
    # path("<int:item_id>/", views.detail, name="detail"),
    path("<int:pk>/", views.FoodDetailView.as_view(), name="detail"),
    path("item/", views.item, name="item"),
    # path('add', views.create_item, name='create_item'),
    path('add', views.FoodCreateView.as_view(), name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
