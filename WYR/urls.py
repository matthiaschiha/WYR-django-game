from django.urls import path
from . import views
from django.contrib import admin

app_name = "WYR"

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("<int:pk>/", views.SCQView.as_view(), name="SCQ"),
    path("<int:scenario_id>/vote/", views.votes, name="votes"),
    path("<int:scenario_id>/next/", views.next_question, name="next"),
    path("<int:scenario_id>/prev/", views.prev_question, name="prev"),
    path("about/", views.AboutView.as_view(), name="about")
]
     