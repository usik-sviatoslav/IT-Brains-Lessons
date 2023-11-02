from rest_framework.routers import DefaultRouter

from contacts.views import ContactViewSet

router = DefaultRouter()
router.register('', ContactViewSet, basename='contact')

urlpatterns = router.urls
