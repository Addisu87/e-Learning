
from django.urls import path

from . import views

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),

    # For updating existing model
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(),
         name='course_module_update'),

    # For creating new content
    path('module/<int:module_id>/content/<model_name>/create/',
         views.ContentCreateUpdateView.as_view(), name='module_content_create'),

    # For updating existing content
    path('module/<int:module_id>/content/<model_name>/<id>/',
         views.ContentCreateUpdateView.as_view(), name='module_content_update'),

    # For delete existing content
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(),
         name='module_content_delete'),

    # For module content list
    path('module/<int:module_id>/', views.ModuleContentListView.as_view(),
         name='module_content_list'),

    # For module drag and drop view
    path('module/order/', views.ModuleOrderView.as_view(), name="module_order"),

    # For content drag and drop view
    path('content/order/', views.ContentOrderView.as_view(), name="content_order"),

    # For displaying all courses for a subject
    path('subject/<slug:subject>/',  views.CourseListView.as_view(),
         name='course_list_subject'),

    # For displaying a single course overview

    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
]
