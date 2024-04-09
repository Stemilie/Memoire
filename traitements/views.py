from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "traitements/index.html")

def main(request):
    return render(request, "index")
def submit_form(request):
    if request.method == 'POST':
        print(request.POST.get('nom'))
        print(request.POST.get('prenom'))
        
    
