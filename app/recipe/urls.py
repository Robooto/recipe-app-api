from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

# router will generate urls from a viewset
router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

# for the reverse function to find the url
app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
