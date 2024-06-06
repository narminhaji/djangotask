from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
from .forms import PortfolioForm

# Create your views here.
def home_view(request):
    return render(request, 'index.html')


def list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'list.html', {'portfolios': portfolios})


def detail(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    return render(request, 'detail.html', {'portfolio': portfolio})


def yarat(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'yarat.html', {'form': form})