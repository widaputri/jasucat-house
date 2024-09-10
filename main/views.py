from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Wida Putri Kinasih',
        'class': 'PBP D',
        'npm': '2306229840',
    }

    return render(request, "main.html", context)