from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

app_name = 'todo-api'

router = DefaultRouter()
router.register('todo', TodoViewSet)

urlpatterns = router.urls