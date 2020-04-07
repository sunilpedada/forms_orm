from django.shortcuts import render
from testapp.models import players
from testapp.form import player_form
# Create your views here.
def home(request):
    queryset=players.objects.get(id=1)
    print(type(queryset))
    return render(request,'testapp/home.html')
def add(request):
    forms_object=player_form()
    if request.method=='POST':
        adding=player_form(request.POST)
        if adding.is_valid():
            adding.save(commit=True)
            return render(request,'testapp/home.html')
        return render(request,'testapp/addplayers.html',{"result":adding})
    return render(request,'testapp/addplayers.html',{"result":forms_object})
def display_list(request):
    get_all=players.objects.all()
    return render(request,'testapp/display.html',{"obj":get_all})
