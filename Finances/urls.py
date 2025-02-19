from django.urls import path,re_path
from . import views



urlpatterns = [
    path("create-credit-card/", views.CreditCardCreateView.as_view(), name="create_cc"),
    path("create-transaction/", views.TransactionCreateView.as_view(), name="create_transaction"),
    path("create-event/", views.EventPlanningCreateView.as_view(), name="create_event"),
    #
    path('edit-credit-card/<int:pk>/', views.CreditCardUpdateView.as_view(), name='cc_edit'),
    path('edit-transaction/<int:pk>/', views.EventPlanningUpdateView.as_view(), name='transaction_edit'),
    path('edit-event/<int:pk>/', views.TransactionUpdateView.as_view(), name='event_edit'),
    #
    path('disable-serie/<int:pk>/', views.set_serie_inactive, name='disable_serie'),
    path('mark-paid/<int:pk>/', views.set_reference_paid, name='mark_paid'),
    #
]



handler404 = 'Finances.views.page_not_found'
handler403 = 'Finances.views.page_forbiden'
handler500 = 'Finances.views.page_error'