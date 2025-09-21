from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # 主界面
    path('news/', views.news_view, name='news'),  # 新闻页面或 API
    path('dining/', views.dining_view, name='dining'),  # 餐厅页面或 API
    path("requirements/", views.grad_requirements, name="grad_requirements"),
    path('pitt-game/', views.pitt_game, name='pitt_game'),
]
