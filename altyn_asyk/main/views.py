from django.shortcuts import render


def index_page(request):
    print("request is accepted")
    return render(request, "main/index2.html", {})


def about(request):
    return render(request, "main/about.html", {})


def bsn(request):
    return render(request, "main/bsn.html", {})


def license(request):
    return render(request, "main/license.html", {})


def community(request):
    return render(request, "main/community.html", {})


def documents(request):
    return render(request, "main/documents.html", {})


def training(request):
    return render(request, "main/training.html", {})


def medicine(request):
    return render(request, "main/medicine.html", {})


def psychology(request):
    return render(request, "main/psychology.html", {})


def covid(request):
    return render(request, "main/covid.html", {})


def bulleten(request):
    return render(request, "main/bulleten.html", {})


def register(request):
    return render(request, "main/register.html", {})


def adaptation(request):
    return render(request, "main/adaptation.html", {})


def security(request):
    return render(request, "main/security.html", {})


def relationship(request):
    return render(request, "main/relationship.html", {})


def schedule(request):
    return render(request, "main/schedule.html", {})


def food_menu(request):
    return render(request, "main/food_menu.html", {})


def open_study(request):
    return render(request, "main/open_study.html", {})


def mornings(request):
    return render(request, "main/mornings.html", {})


def zhangyru(request):
    return render(request, "main/zhangyru.html", {})


def aula(request):
    return render(request, "main/aula.html", {})


def ish(request):
    return render(request, "main/ish.html", {})


def top(request):
    return render(request, "main/top.html", {})