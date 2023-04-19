from django.shortcuts import render,redirect
from hi.forms import NameForm
from hi.models import Name

# Create your views here.

def hi(request):
    names = Name.objects.all()
    return render(request, 'hi.html',context={'names':names})

def name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hi')
    form=NameForm()
    return render(request, 'name.html',context={"form":NameForm})