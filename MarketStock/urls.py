from django.contrib import admin
from django.urls import path
import dashboard.views
import market.views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard.views.index, name='Главная страница'),
    path('market/', dashboard.views.market, name='Супермаркеты'),
    path('market/detail/<int:pk>/', dashboard.views.market_detail, name='Посмотреть'),
    path('market/delete/<int:pk>/', dashboard.views.market_delete, name='Удалить маркет'),
    path('product/', dashboard.views.product, name='Продукты'),
    path('product/delete/<int:pk>/', dashboard.views.product_delete, name='Удалить продукт'),
    path('products/edit/<int:pk>/', dashboard.views.product_edit, name='Изменить продукт'),
    path('order/', dashboard.views.order, name='Поставки'),
    path('order/delete/<int:pk>/', dashboard.views.order_delete, name='Удалить заказ'),
    path('register/', market.views.register, name='Регистрация'),
    path('', auth_views.LoginView.as_view(template_name='market/login.html'), name='Вход'),
    path('logout/', auth_views.LogoutView.as_view(template_name='market/logout.html'), name='Выход'),
    path('profile/', market.views.profile, name='Профиль'),
    path('profileupd/', market.views.profile_update, name='Изменить профиль')
]
