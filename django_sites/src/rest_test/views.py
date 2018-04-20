from django.core.cache import cache
from django.shortcuts import redirect
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


# Create your views here.

class IndexView(GenericAPIView):

    def get(self, request):
        # ts = TestSerilalizer(data=request.query_params)
        # ts.is_valid()
        cache_key = 'rest_test:site-hit'
        site_hit = cache.get(cache_key)
        if not site_hit:
            site_hit = 0
        site_hit += 1
        cache.set(cache_key, site_hit)
        return redirect('redirect/@@/{}'.format(site_hit))


class RedirectView(GenericAPIView):

    def get(self, request, num):
        message = 'This is the redirected resource. your num is {}'.format(num)
        return Response({'message': message})