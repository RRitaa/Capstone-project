from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter 

from rest_framework.authtoken.views import obtain_auth_token

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='name-item'),
    path('menu-items/', views.MenuItemsView.as_view()),
    
    path('booking/', include(router.urls) ),
    path('restaurant/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]