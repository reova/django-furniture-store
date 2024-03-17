from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Home ',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - About us',
        'content': 'About us',
        'text_on_page': 'about about about us'
    }
    
    return render(request, 'main/about.html', context)
