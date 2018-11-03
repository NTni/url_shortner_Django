from django.http import HttpResponse
from.models import Superheroes

def avengers(request):
    all_Superheroes = Superheroes.objects.all()
    for a in all_Superheroes:
        url = 'marvel' + str (a.id)+'/'
        html = '<a href ="'+url+'">' + a.Team +'</a><br>'
    return HttpResponse("<h1> marvel </h1>")
def hero(request):
    return HttpResponse("<h2> avengers-fantastic4-xmen </h2>")
def villain(request):
    return HttpResponse("<h1><b><i> thanos</i></b> </h1>")