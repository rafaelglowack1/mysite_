from django.http import HttpResponse
from django.views import generic


class ProductView(generic.View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('The Elder Scrolls V: Skyrim (ansioso pra aprender a colocar um .html aqui)')
