from django.conf.urls import url
from .views import GetBatchTransaction, BatchTransactions

urlpatterns = [
    url(r'^(?P<batch_trid>[a-fA-F0-9]{8}-?[a-fA-F0-9]{4}-?[1345][a-fA-F0-9]{3}-?[a-fA-F0-9]{4}-?[a-fA-F0-9]{12})$',
        GetBatchTransaction.as_view(),
        name='get_batch_transaction'),
    url(r'^(?P<batch_trid>[a-fA-F0-9]{8}-?[a-fA-F0-9]{4}-?[1345][a-fA-F0-9]{3}-?[a-fA-F0-9]{4}-?[a-fA-F0-9]{12})/(?P<state>[\w\-]+)$',
        GetBatchTransaction.as_view(),
        name='get_batch_transaction_by_state'),
    url(r'$', BatchTransactions.as_view(), name='batchtransactions'),
]

