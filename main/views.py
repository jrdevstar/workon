from django.shortcuts import render

def homepage(request):
    context={}
    return render(request, 'main/homepage.html', context)


def PortfolioDetail(request):
    context={

    }
    return render(request, 'main/portfolio-details.html', context)