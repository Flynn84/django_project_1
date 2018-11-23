from django.shortcuts import render

posts = [
    {
        'author': 'Jack Lemmon',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 23, 2018'
    },
    {
        'author': 'Jim Jameson',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 24, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
