from django.shortcuts import render


def posts_list(request):
    names = ['Ivan', 'Sergey', 'Oleg', 'Dmitry', 'Artem']
    return render(request, 'blog/index.html', context={'names': names})
