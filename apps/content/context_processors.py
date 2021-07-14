from .models import WebSites


def web_sites(request):
    web_sites = WebSites.objects.all()

    return {'web_sites': web_sites}

