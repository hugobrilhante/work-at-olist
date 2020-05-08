from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import SimpleRouter

from .apps.authors import views as author
from .apps.base import views as base
from .apps.books import views as book

routes = SimpleRouter(trailing_slash=True)

routes.register('authors', author.AuthorViewSet, 'author')
routes.register('books', book.BookViewSet, 'book')

api_patterns = [
    path('', include(routes.urls))
]

schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='v1',
        description="Api for Library",
    ),
    patterns=api_patterns,
    public=True,
    authentication_classes=(BasicAuthentication,),
    permission_classes=(IsAuthenticated,)
)

urlpatterns = [
    path('', base.APIRootView.as_view()),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs')
]

urlpatterns += api_patterns
