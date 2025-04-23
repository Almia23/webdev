from django.shortcuts import render
from .forms import PromoForm
import datetime

def promo_view(request):
    form = PromoForm()
    result = ''
    if request.method == "POST":
        form = PromoForm(request.POST)
        if form.is_valid():
            doj = form.cleaned_data['doj']
            years = (datetime.date.today() - doj).days / 365
            result = "YES" if years >= 5 else "NO"
    return render(request, 'main/promo.html', {'form': form, 'result': result})