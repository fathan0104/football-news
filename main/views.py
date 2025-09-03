from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406496284',
        'name': 'Fathan Alfahrezi',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
