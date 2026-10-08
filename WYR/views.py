from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import random
# Create your views here.
from .models import Scenario, Category

# Create your views here.
class Index(generic.View):
    model = Scenario
    template_name = "WYR/index.html" 
    def get(self, request):
        question = get_object_or_404(Scenario, pk=1)
        return render(
            request,
            "WYR/index.html",
            {
                "scenario":question,
            }

        )
       
class SCQView(generic.DetailView):
    model = Scenario
    category_filter = Category
    template_name = "WYR/SCQ.html"

class VotesView(generic.DetailView):
    model = Scenario
    template_name = "WYR/votes.html"

class AboutView(generic.DetailView):
    model = Scenario
    template_name = "WYR/about.html"
    def get(self, request):
        question = get_object_or_404(Scenario, pk=1)
        return render(
            request,
            "WYR/about.html",
            {
                "scenario":question,
            }

        )


def votes(request, scenario_id):

    question = get_object_or_404(Scenario, pk=scenario_id)
    try:
        selected = request.POST["choice"]
    except (KeyError):
        return render(
            request,
            "WYR/SCQ.html",
            {
                "scenario":question,
                "option_1":question.scenario_question_1,
                "option_2":question.scenario_question_2,

                "error_message":"Select a proper option"
            },
        )
    else:
        if selected == "uno":
            question.votesQ1 +=1
            question.save()
        elif selected == "dos": 
            question.votesQ2 +=1
            question.save()

    print(selected)
    
    return TotalVotes(request,scenario_id)

def TotalVotes(request, scenario_id):
    question = get_object_or_404(Scenario, pk=scenario_id)
    votes = question.votesQ1 + question.votesQ2

    vote_percent1 = round((question.votesQ1/votes)*100, 2)
    vote_percent2 = round((question.votesQ2/votes)*100, 2)

    return render(
        request,"WYR/votes.html",
        {
            "scenario":question,
            "option_1":question.scenario_question_1,
            "option_2":question.scenario_question_2,
            "Votes_1":question.votesQ1,
            "Votes_2":question.votesQ2,
            "unopercentage":vote_percent1,
            "dospercentage":vote_percent2,
            "Total_Votes":votes,

        }
    )

#button to the next question
def next_question(request, scenario_id):
    current_question = get_object_or_404(Scenario, pk=scenario_id)
    questions = list(Scenario.objects.order_by("date_published"))
    position = questions.index(current_question)
    print(len(questions))
#^ Get the current question
    if position >= len(questions)-1:
        return render(
            request,
            "WYR/SCQ.html",
            {
                "scenario":current_question,
                "error_message":"You have reached the end of the Questions"
            },
        )
    else:
        next_question = questions[position +1]

    return HttpResponseRedirect(reverse("WYR:SCQ", args=(next_question.id,)))
    #move on to the next one by increasing the index of the latest questions


def prev_question(request, scenario_id):
    current_question = get_object_or_404(Scenario, pk=scenario_id)
    questions = list(Scenario.objects.order_by("date_published"))
    position = questions.index(current_question)
#^ Get the current question
    if position == 0:
        return render(
            request,
            "WYR/SCQ.html",
            {
                "scenario":current_question,
                "error_message":"You have reached the start of the Questions"
            },
        )
    else:
        prev_question = questions[position -1]

    return HttpResponseRedirect(reverse("WYR:SCQ", args=(prev_question.id,)))
    #move back to the next one by decreasing the index of the latest questions
    