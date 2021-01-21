from django.urls import path, include
from preadmission.views import ApplicationViewSet, SubmitApplicationViewSet

urlpatterns = [
    path('enquiry/', ApplicationViewSet.as_view({'post':'create'}), name='enquiry_form'),
    path('all-enquiries/', ApplicationViewSet.as_view({'get':'list'}), name='enquiries'),
    path('get-application-data/<pk>', ApplicationViewSet.as_view({'get':'retrieve'}), name='get_enquiry'),
    path('verify-enquiry-application/<pk>', ApplicationViewSet.as_view({'put':'update'}), name='enquiry_verify'),
    path('submit-application/<reference_number>', SubmitApplicationViewSet.as_view({'put':'update'}), name='submit_application'),
]
