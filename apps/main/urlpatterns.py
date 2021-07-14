""" # todo resolve ve reverse ile path ayarla
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.content.urls import urlpatterns as content_url
from apps.content.urls import app_name as content_name
from t3bilimturkiye.urls import urlpatterns as t3bilimturkiye_url
from t3bilimturkiye.urls import app_name as t3bilimturkiye_name

urlpatterns_content = content_url[:-1]

content = tuple((str(content_name + ':' + url.name), str(content_name + ':' + url.name)) for url in urlpatterns_content)
t3 = tuple(
    (str('content' + ':' + t3bilimturkiye_name + ':' + url.name), str(t3bilimturkiye_name + ':' + url.name)) for url in
    t3bilimturkiye_url)
urls = t3 + content


def validate_slug(slug):
    # todo custom sub menu sluglarını kontrol et
    patterns = urlpatterns_content + t3bilimturkiye_url
    if slug in [url.name for url in patterns]:
        print(slug)
        raise ValidationError(
            _('Bu url adında tanımlanmış bir url olduğu için bu kısmı lütfen değiştirin.'),
            params={'value': slug},
        )
 """