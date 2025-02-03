from django.urls import path
from django.shortcuts import redirect  # Correct import for redirect
from . import views

app_name = 'compiler'

urlpatterns = [
    path('', lambda request: redirect('compiler:editor')),  # Redirect `/compiler/` to `/compiler/editor/`
    path('editor/', views.editor_view, name='editor'),
    path('api/execute/', views.ExecuteCodeView.as_view(), name='execute-code'),
    path('api/history/', views.CodeHistoryView.as_view(), name='code-history'),
]
