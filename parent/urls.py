from django.urls import path
from parent import views

urlpatterns = [
    path('create_parent/', views.ParentCreateView.as_view(), name='create-parent'),
    path('list_of_parents/', views.ParentsListView.as_view(), name='list-of-parents'),
    path('update_parent/<int:pk>/', views.ParentUpdateView.as_view(), name='update-parent'),
    path('delete_parent/<int:pk>/', views.ParentDeleteView.as_view(), name='delete-parent'),
    path('details_parent/<int:pk>/', views.ParentDetailView.as_view(), name='details-parent'),
]

