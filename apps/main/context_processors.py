from apps.main.models import Menu, SiteInfo


def site(request):
    site_info = SiteInfo.objects.first()
    return {'site_info': site_info}


def menu(request):
    header_menu_list = Menu.objects.filter(menu_location_id=1).translate(
        request.LANGUAGE_CODE).order_by('alignment')
    footer_menu_list = Menu.objects.filter(menu_location_id=2).translate(
        request.LANGUAGE_CODE).order_by('alignment')

    return {'header_menu_list': header_menu_list, 'footer_menu_list': footer_menu_list}
