from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'category',views.CategoryViewSet,basename='category')
router.register(r'kind',views.KindViewSet,basename='kind')
router.register(r'subkind',views.SubkindViewSet,basename='subkind')
router.register(r'priority',views.PriorityViewSet,basename='priority')
router.register(r'status',views.StatusViewSet,basename='status')
router.register(r'person',views.PersonViewSet,basename='person')
router.register(r'ticket',views.TicketViewSet,basename='ticket')


urlpatterns = [
    path('', include(router.urls)),
]
