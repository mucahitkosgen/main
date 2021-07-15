from django.conf.urls import url

app_name = 'accounts'

url_patterns= [
    url(r'^sign_in/$', sign_in_view, name='sign_in'),

]