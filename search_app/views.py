from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from movie_app.models import Movie

def search(request, search_type, search):
    if search_type == 'genre':
        movies = Movie.objects.filter(genres__name__contains=search)
    elif search_type == 'production':
        movies = Movie.objects.filter(productions__name__contains=search)
    elif search_type == 'cast':
        movies = Movie.objects.filter(casts__name__contains=search)
    elif search_type == 'director':
        movies = Movie.objects.filter(directors__name__contains=search)
    elif search_type == 'rating':
        movies = Movie.objects.filter(rating=search)
    elif search_type == 'country':
        movies = Movie.objects.filter(countries__name__contains=search)

    paginator = Paginator(movies, 12)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "search": search,
    }
    return render(request, 'result.html', context) 