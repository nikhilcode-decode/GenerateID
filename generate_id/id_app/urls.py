# id_card_generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate-id-card/', views.generate_id_card, name='generate_id_card'),
path('generate_id/generate_id_card/', views.generate_id_card, name='generate_id_card'),  # Your custom URL
]
