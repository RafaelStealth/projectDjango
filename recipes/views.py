from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')

    messages.success(request, 'Epa, você foi pesquisar algo que eu vi.')

    recipes = Paginator(recipes, 9)
    page_number = request.GET.get('page')
    page_obj = recipes.get_page(page_number)
    print(page_obj)

    return render(request, 'recipes/pages/home.html', {
        'recipes': page_obj,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    recipes = Paginator(recipes, 9)
    page_number = request.GET.get('page')
    page_obj = recipes.get_page(page_number)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'is_detail_page': False,
    })


def recipe(request, id):
    #  recipes = Recipe.objects.filter(id=id, is_published=True).first()
    recipes = get_object_or_404(Recipe, id=id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipes,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(title__icontains=search_term) | # noqa: W504, E261
        Q(description__icontains=search_term) | # noqa: W504, E261
        Q(category__name__icontains=search_term),
    ).order_by('-id')

    return render(
        request, 'recipes/pages/search.html',
        {'page_title': f'Search for "{search_term}" |',
         'search_term': search_term,
         'recipes': recipes,
         })
