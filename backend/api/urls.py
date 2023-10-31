from django.urls import include, path, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="Career Tracker Hackathon",
        default_version='v1',
        description="Schema API for Career Tracker Hackathon",
        contact=openapi.Contact(email="i@msavilov.ru"),
        license=openapi.License(name="Apache License 2.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


v1_router = DefaultRouter()

# v1_router.register('vacancies', VacanciesViewSet, basename='vacancies')


urlpatterns = [
    path('', include(v1_router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
