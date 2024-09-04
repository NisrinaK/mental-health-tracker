from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275456',
        'name': 'Nisrina Kamilya Nisyya',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
