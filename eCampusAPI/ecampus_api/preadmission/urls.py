from django.urls import path, include
from preadmission.views import ApplicationViewSet, SubmitDocsViewSet, ApproveOrRejectDoc

urlpatterns = [
    path('enquiry/', ApplicationViewSet.as_view({'post':'create'}), name='enquiry_form'),
    path('all-enquiries/', ApplicationViewSet.as_view({'get':'list'}), name='enquiries'),
    path('get-application/<pk>/', ApplicationViewSet.as_view({'get':'retrieve'}), name='get_enquiry'),
    path('update-enquiry-application/<pk>/', ApplicationViewSet.as_view({'put':'update'}), name='enquiry_verify'),
    path('submit-application/<id>/<application_token>/', SubmitDocsViewSet.as_view({'put':'update'}), name='submit_application'),
    path('approve-or-reject-doc/<id>/', ApproveOrRejectDoc.as_view({'put':'update'}), name='docs_verify'),
]
