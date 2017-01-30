from django.shortcuts import render
from partner.models import Partner

# Create your views here.
def index(request):
    category = request.GET.get("category")

    partner_list = Partner.objects.filter(user__is_active = True)

    if(category):
     partner_list = partner_list.filter(category = category)

    category_list = list(Partner.CATEGORY_CHOICES)

    ctx = {
        "partner_list" : partner_list,
        "category_list": category_list
    }
    return render(request, "main.html", ctx)