from django.urls import path
from .views import HomeView, AboutView, ServiceView, BlogView, BlogSingleView, PricingView, PortfolioView, \
    PortfolioDetailView, TeamView, ContactView, detailview

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('<int:pk>/', detailview, name='detail'),
    path('service/', ServiceView.as_view(), name='service'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-single/', BlogSingleView.as_view(), name='blog-single'),
    path('price/', PricingView.as_view(), name='price'),
    path('service/', ServiceView.as_view(), name='service'),
    path('plant/', PortfolioView.as_view(), name='plant'),
    path('<int:pk>/plant-detail/', PortfolioDetailView.as_view(), name='plant-detail'),
    path('team/', TeamView.as_view(), name='team'),
    path('contact/', ContactView.as_view(), name='contact'),
]
