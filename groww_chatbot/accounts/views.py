from django.shortcuts import render

# Create your views here.
def loginorregister(request):
    return render(request, 'website/loginandregister.html')