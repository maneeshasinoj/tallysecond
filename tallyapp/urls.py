from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('company',views.company,name='company'),
    path('base',views.base,name='base'),
    path('createcompany',views.createcompany,name='createcompany'),
    path('companycreate',views.companycreate,name='companycreate'),
    path('group/<int:pk>',views.group,name='group'),
    path('ledger/<int:pk>',views.ledger,name='ledger'),
    path('costcentre/<int:pk>',views.costcentre,name='costcentre'),
    path('currency/<int:pk>',views.currency,name='currency'),
    path('features/<int:pk>',views.features,name='features'),
    path('creategroup/<int:pk>',views.creategroup,name='creategroup'),
    # path('features',views.features,name='features'),
    path('altercompanyview',views.altercompanyview,name='altercompanyview'),
    path('selectcompany',views.selectcompany,name='selectcompany'),
    path('shutcompany',views.shutcompany,name='shutcompany'),
    path('addstate',views.addstate,name='addstate'),
    path('addcountry',views.addcountry,name='addcountry'),
    path('altercompany/<int:pk>',views.altercompany,name='altercompany'),
    path('ratesofexchange/<int:pk>',views.ratesofexchange,name='ratesofexchange'),
    path('voucher/<int:pk>',views.voucher,name='voucher'),
    path('democreate',views.democreate,name='democreate'),
    path('demo1/<int:pk>',views.demo1,name='demo1'),
    # path('demo2/<int:pk>',views.demo2,name='demo2'),
    path('featurecompany/<int:pk>',views.featurecompany,name='featurecompany'),
    path('disable/<int:pk>',views.disable,name='disable'),
    path('enable/<int:pk>',views.enable,name='enable'),

    path('alter',views.alter,name='alter'),
    path('altercompany_view',views.altercompany_view,name='altercompany_view'),
    path('listofgroup',views.listofgroup,name='listofgroup'),
    path('listofledgers',views.listofledgers,name='listofledgers'),
    path('listofcostcentres',views.listofcostcentres,name='listofcostcentres'),
    path('listofcurrencies',views.listofcurrencies,name='listofcurrencies'),
    path('listofvouchertypes',views.listofvouchertypes,name='listofvouchertypes'),
    path('alter_create_group/<int:pk>',views.alter_create_group,name='alter_create_group'),
    path('vouchers/<int:pk>',views.vouchers,name='vouchers'),
    path('creditnote/<int:pk>',views.creditnote,name='creditnote'),
    path('debitenote',views.debitenote,name='debitenote'),
    path('receiptdetails',views.receiptdetails,name='receiptdetails'),
    path('partydetails',views.partydetails,name='partydetails'),
    path('debitnoteregister/<int:pk>',views.debitnoteregister,name='debitnoteregister'),
    path('creditnoteregister/<int:pk>',views.creditnoteregister,name='creditnoteregister'),
    path('date',views.date,name='date'),
    path('add_receiptdetails',views.add_receiptdetails,name='add_receiptdetails'),
    path('displaymore/<int:pk>',views.displaymore,name='displaymore'),
    path('accountbook/<int:pk>',views.accountbook,name='accountbook'),
    path('voucherregister',views.voucherregister,name='voucherregister'),
    path('voucherregisterdebit',views.voucherregisterdebit,name='voucherregisterdebit'),
    path('creditsave',views.creditsave,name='creditsave'),
    path('add_partydetails',views.add_partydetails,name='add_partydetails'),
]
