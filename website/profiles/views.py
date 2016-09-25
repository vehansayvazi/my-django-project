from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Program, Team, Player, Coach

def index(request):
    all_program = Program.objects.all()
    all_team = Team.objects.all()
    all_player = Player.objects.all()

    team7u = Player.objects.all().order_by('number').filter(team__name='7u Team') #need to use team__name becaue team is a ForeignKey to Team
    team8u = Player.objects.all().order_by('number').filter(team__name='8u Team') #need to use team__name becaue team is a ForeignKey to Team
    team9u = Player.objects.all().order_by('number').filter(team__name='9u Team')
    team10u = Player.objects.all().order_by('number').filter(team__name='10u Team')
    team11u = Player.objects.all().order_by('number').filter(team__name='11u Team')
    team12u = Player.objects.all().order_by('number').filter(team__name='12u Team')
    team13u = Player.objects.all().order_by('number').filter(team__name='13u Team')
    team14u = Player.objects.all().order_by('number').filter(team__name='14u Team')
    team15u = Player.objects.all().order_by('number').filter(team__name='15u Team')
    team16u = Player.objects.all().order_by('number').filter(team__name='16u Team')
    team17u = Player.objects.all().order_by('number').filter(team__name='17u Team')

    context = {'all_program': all_program, 'all_team': all_team, 'all_player': all_player,
               'team7u': team7u, 'team8u': team8u, 'team9u': team9u, 'team10u': team10u, 'team11u': team11u,
               'team12u': team12u, 'team13u': team13u, 'team14u': team14u,'team15u': team15u,
               'team16u': team16u,'team17u': team17u,}

    return render(request, 'profiles/index.html', context)


# def program_detail(request, program_id):
#     all_team = Team.objects.all()
#     program = get_object_or_404(Program, pk=program_id)
#
#     print Player.objects.all()
#
#     return render(request, 'profiles/program_detail.html', {'program': program, 'all_team' : all_team})
#     #return HttpResponse("program detail")
#
# def team_detail(request, team_id):
#     all_player = Player.objects.all()
#     team = get_object_or_404(Team, pk=team_id)
#     return render(request, 'profiles/team_detail.html', {'team': team, 'all_player' : all_player})
#     #return HttpResponse("program detail")
#
# def player_detail(request, player_id):
#     player = get_object_or_404(Player, pk=player_id)
#     return render(request, 'profiles/player_detail.html', {'player': player})
#     #return HttpResponse("program detail")
