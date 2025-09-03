from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406344542',
        'name': 'Petrus Wermasaubun',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)