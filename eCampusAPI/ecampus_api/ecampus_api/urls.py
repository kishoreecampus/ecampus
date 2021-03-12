"""ecampus_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import HttpResponse
from preadmission.models import Application
from student.models import Document
import os

schema_view = get_schema_view(
   openapi.Info(
      title="eCampus API",
      default_version='v1',
      description="eCampus API services",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('accounts/', admin.site.urls),
    path('authentication/', include('api_authentication.urls')),
    path('', include('roles_and_permission.urls')),
    path('modules/', include('modules.urls')),
    path('master/', include('master.urls')),
    path('employee/', include('employee.urls')),
    path('pre-admission/', include('preadmission.urls')),
    path('', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    path('api-documents/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

def protected_document_serve(request, docid, path, document_root=None):
    try:
        app_obj = Application.objects.get(application_token=request.GET.get('token'), reference_number=request.GET.get('ref'))
        doc_obj = Document.objects.get(id=app_obj.docs_id)
        correct_image_url = getattr(doc_obj, request.GET.get('target')).url.replace("/media/", "")
        full_path = os.path.join('uploads/'+ request.GET.get('dir') + '/', str(doc_obj.id)) + "/" + path
        if correct_image_url == full_path:
            return serve(request, full_path, document_root)
        return HttpResponse("File not found")
    except ObjectDoesNotExist:
        return HttpResponse("File not found")

urlpatterns += [
    path('media/uploads/documents/<docid>/<path>', protected_document_serve, {'document_root': settings.MEDIA_ROOT}),
]
