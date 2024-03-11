from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("auth/", include("apps.api.auth.v1")),
    path("company/", include("apps.api.company.v1")),
    path("employees/", include("apps.api.employees.v1")),
]
