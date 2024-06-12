from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
   peoples = [
       {'sn':1,'name':'Pranjal Barnwal','age':20},
       {'sn':2,'name':'Suman phuyal','age':21},
       {'sn':3,'name':'Yugal neupane','age':22},
       {'sn':4,'name':'Roshan Gupta','age':21},
   ]
   vegetables={'cucumber','tomato','brinjal'}
   text={"""Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quisquam ipsum, officiis natus consectetur magni atque aliquid molestias, obcaecati aut repellendus in provident dolore illo ea laborum! Voluptatibus laborum iste obcaecati? Expedita, alias, molestias iure debitis culpa est laudantium corporis magni assumenda quo repellat cupiditate dolores, vel natus veniam qui architecto beatae placeat laborum vitae obcaecati molestiae. Labore, sequi exercitationem illum soluta repellendus, minima optio voluptates expedita delectus cumque unde, dolor eligendi ullam nemo odit ratione. Ipsa similique quod nostrum eveniet? Beatae quam perspiciatis sed sint vitae excepturi quae libero aspernatur quidem, ab quaerat provident id laborum explicabo et, repellat rerum!
"""}
   return render(request,"home/index.html", context={'page':'Home','peoples':peoples,'vegetables':vegetables,"text":text})

def success_page(request):
    return HttpResponse("<h1>Hey This is success page</h1>")

def contact(request):
    return render(request,"home/contact.html", context  ={'page':'Contact'})

def about(request):
    return render(request,"home/about.html",  context   ={'page':'About'})