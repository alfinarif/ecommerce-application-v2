from django.urls import path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('index/', views.DashboardIndexView.as_view(), name='dashboard_index'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('product/add-new/', views.AddNewProduct.as_view(), name='add_new_product'),
    path('product/update/<slug:slug>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<slug:slug>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('categories/', views.CategoryListView.as_view(), name='category'),
    path('categories/add-new/', views.AddNewCategory.as_view(), name='add_new_category'),
    path('categories/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),
]
