from django.shortcuts import render
#from django.http import HttpResponse
from dta.forms import transferfrom

# Create your views here.
def index(request):
    #return HttpResponse("Check this shit out")
    form = transferfrom()
    return render(request, 'dta/index.html', {'form': form})


