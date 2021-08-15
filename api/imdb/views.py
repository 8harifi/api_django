from django.http import HttpResponse, JsonResponse
from api.imdb.api.imdb_api import imdb


def search(request):
    if request.method == "GET":
        return HttpResponse("only POST requests can be accepted")
    elif request.method == "POST":
        q = request.POST.get("q")
        s = imdb.search(q)
        id = s[0]['id']
        return JsonResponse({'id': id})




