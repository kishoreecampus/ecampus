from django.urls import path, include
from .views import ProfileViewSet,ClassGroupViewset,ClassNameViewset,SectionViewset,CategoryViewset,CasteViewset

urlpatterns = [
    path('profile/list/', ProfileViewSet.as_view({'get':'list'}), name='list_profile'),
    path('profile/detail/<pk>/', ProfileViewSet.as_view({'get':'retrieve'}), name='profile'),
    path('profile/create/', ProfileViewSet.as_view({'post':'create'}), name='create_profile'),
    path('profile/update/<pk>/', ProfileViewSet.as_view({'put':'update'}), name='update_profile'),
    path('profile/delete/<pk>/', ProfileViewSet.as_view({'delete':'destroy'}), name='delete_profile'),
    path('class_group/create/', ClassGroupViewset.as_view({'post':'create'}), name='Create_class_group'),
    path('class_group/list/', ClassGroupViewset.as_view({'get':'list'}), name='list_class_group'),
    path('class_group/detail/<pk>/', ClassGroupViewset.as_view({'get':'retrieve'}), name='detail_class_group'),
    path('class_group/update/<pk>/', ClassGroupViewset.as_view({'put':'update'}), name='update_class_group'),
    path('class_group/delete/<pk>/', ClassGroupViewset.as_view({'delete':'destroy'}), name='delete_class_group'),
    path('class_name/create/', ClassNameViewset.as_view({'post':'create'}), name='Create_class_name'),
    path('class_name/list/', ClassNameViewset.as_view({'get':'list'}), name='list_class_name'),
    path('class_name/detail/<pk>/', ClassNameViewset.as_view({'get':'retrieve'}), name='detail_class_name'),
    path('class_name/update/<pk>/', ClassNameViewset.as_view({'put':'update'}), name='update_class_name'),
    path('class_name/delete/<pk>/', ClassNameViewset.as_view({'delete':'destroy'}), name='delete_class_name'),
    path('section/create/',SectionViewset.as_view({'post': 'create'}), name='Create_class_section'),
    path('section/list/',SectionViewset.as_view({'get': 'list'}), name='list_class_section'),
    path('section/detail/<pk>/',SectionViewset.as_view({'get': 'retrieve'}), name='detail_class_section'),
    path('section/update/<pk>/',SectionViewset.as_view({'put': 'update'}), name='update_class_section'),
    path('section/delete/<pk>/',SectionViewset.as_view({'delete': 'destroy'}), name='delete_class_section'),
    path('Category/create/',CategoryViewset.as_view({'post': 'create'}), name='Create_Category'),
    path('Category/list/',CategoryViewset.as_view({'get': 'list'}), name='list_Category'),
    path('Category/detail/<pk>/',CategoryViewset.as_view({'get': 'retrieve'}), name='detail_Category'),
    path('Category/update/<pk>/',CategoryViewset.as_view({'put': 'update'}), name='update_Category'),
    path('Category/delete/<pk>/',CategoryViewset.as_view({'delete': 'destroy'}), name='delete_Category'),
    path('Caste/create/',CasteViewset.as_view({'post': 'create'}), name='Create_Caste'),
    path('Caste/list/',CasteViewset.as_view({'get': 'list'}), name='list_Caste'),
    path('Caste/detail/<pk>/',CasteViewset.as_view({'get': 'retrieve'}), name='detail_Caste'),
    path('Caste/update/<pk>/',CasteViewset.as_view({'put': 'update'}), name='update_Caste'),
    path('Caste/delete/<pk>/',CasteViewset.as_view({'delete': 'destroy'}), name='delete_Caste'),


]