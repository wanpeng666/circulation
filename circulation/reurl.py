from django.http import HttpResponseRedirect


def re_url_to(request):
    return HttpResponseRedirect('admin/')
