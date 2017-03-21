from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.CustomerWalletViewSet.as_view(),
        name="list_customer_wallet"),
    url(r'^(?P<pk>[0-9]+)/$',
        views.CustomerWalletViewSet.as_view(),
        name="customer_wallet_detail"),
    url(r'^msisdn/(?P<msisdn>[0-9]+)/status/$',
        views.GetAccountStatusByMsisdn.as_view(),
        name="get_account_status_by_msisdn"),
    url(r'^(?P<wallet_id>[0-9a-zA-z\-]+)/status/$',
        views.GetAccountStatusByAccountId.as_view(),
        name="get_account_status_by_account_id"),
    url(r'^msisdn/(?P<msisdn>[0-9]+)/accountname/$',
        views.GetAccountNameByMsisdn.as_view(),
        name="get_account_name_by_msisdn"),
    url(r'^(?P<account_id>[\w\-]+)/accountname/$',
        views.GetAccountNameByAccountId.as_view(),
        name="get_account_name_by_account_id"),
    url(r'^msisdn/(?P<msisdn>[0-9]+)/balance/$',
        views.AccountBalanceByMsisdn.as_view(),
        name="get_account_balance_by_msisdn"),
    url(r'^msisdn/(?P<msisdn>[0-9]+)/transactions/$',
        views.AccountTransactionsByMsisdn.as_view(),
        name="get_account_transactions_by_msisdn"),
    url(r'^(?P<account_id>[0-9A-Za-z\-]+)/transactions/$',
        views.AccountTransactionsByAccountId.as_view(),
        name="get_account_transactions_by_account_id"),
    url(r'^(?P<account_id>[\w\-]+)/balance/$',
        views.AccountBalanceByAccountId.as_view(),
        name="get_account_balance_by_account_id"),
    url(r'^msisdn/(?P<msisdn>[0-9]+)/statemententries/$',
        views.GetStatementEntriesByMsisdn.as_view(),
        name="get_statement_by_msisdn"),
    url(r'^(?P<wallet_id>[0-9a-zA-z\-]+)/statemententries/$',
        views.GetStatementEntriesByAccountID.as_view(),
        name="get_statement_by_account_id"),
    url(r'^msisdn/(?P<msisdn>[0-9]+)/bills/$',
        views.GetBillsByMsisdn.as_view(),
        name="get_bills_by_msisdn"),
    url(r'^(?P<wallet_id>[0-9a-zA-z\-]+)/bills/$',
        views.GetBillsByAccountID.as_view(),
        name="get_bills_by_account_id"),
]
