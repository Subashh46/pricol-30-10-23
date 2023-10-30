from django.urls import path
from .views import HomePageView, StatusPageView, MachineDetailView, NewStatusView, DocumentListView, ScanPageView, \
                    HistoryPageView, scan_view, PlantDetailView, LineDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('status/', StatusPageView.as_view(), name='status'),
    path('plant/<int:pk>/', PlantDetailView.as_view(), name='plant_detail'),
    path('plant/line/<int:pk>', LineDetailView.as_view(), name='line_detail'),
    path('machines/<int:pk>/', MachineDetailView.as_view(), name='machine_detail'),
    path('new/', NewStatusView.as_view(), name='new_status'),
    # path('machine/<int:pk>/update/', UpdateStatusView.as_view(), name='update_status'),
    # path('machine/<int:pk>/delete/', DeleteStatusView.as_view(), name='delete_status'),
    path('machines/documents/', DocumentListView.as_view(), name='documents'),
    path('scan', ScanPageView.as_view(), name='scan'),
    path('history/', HistoryPageView.as_view(), name='history'),
    path('my-action/', scan_view, name='my_action_view'),
]
