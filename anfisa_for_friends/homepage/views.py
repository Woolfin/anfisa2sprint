from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = 'homepage/index.html'
    ice_cream_list = (
        IceCream.objects.values(
            'id', 'title', 'description', 'category__title', 'wrapper__title',
            'price'
            )
        .filter(
            is_published=True, is_on_main=True, category__is_published=True
        ).order_by('title')[:3]
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)
