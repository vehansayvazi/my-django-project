from django.http import HttpResponse
from django.template import loader
from .models import Group

def index(request):
    all_groups = Group.objects.all()
    template = loader.get_template('profiles/index.html')
    context = {
        'all_groups': all_groups,
    }
    return HttpResponse(template.render(context, request))

def detail(request, group_id):
    return HttpResponse("<h2>the group name is: " + str(group_id) + "</h2>")