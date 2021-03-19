from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import  View,TemplateView, ListView,DeleteView
from django.views.generic.detail import DetailView


from .models import Pet, PetOwner

## Create your views here.
def list_pet_owners(request):
    """List owners."""
    owner = PetOwner.objects.all()
    context = {"owners": owner}

    template = loader.get_template("vet/owners/list.html")
    return HttpResponse(template.render(context, request))

##vista como clase de owners
class Owners(View):
    def get(self,request):
        owner = PetOwner.objects.all()
        context = {"owners": owner}
        template = loader.get_template("vet/owners/list.html")
        return HttpResponse(template.render(context, request))


##template views

# class Owners_List(TemplateView):
#     template_name = "vet/owners/list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context)#esto viene del contexto del padre
#         context['owners']= PetOwner.objects.all()
#         print(context)#esto del que nosotros creamos  context{'owners':owner} #owner = PetOwner.objects.all()
#         return context


##vistas genericas basadas en clases

class Owners_List(ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"

##
class Owners_Detail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = 'owner'



############pet list
class PetList(TemplateView):
    template_name = "vet/pets/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)#esto viene del contexto del padre
        context['peet']= Pet.objects.all()
        print(context)#esto del que nosotros creamos  context{'owners':owner} #owner = PetOwner.objects.all()
        return context

############pet detail
class PetDetail(TemplateView):
    template_name = "vet/pets/pet_detail.html"
    def get_context_data(self,id,**kwargs):
        context = super().get_context_data(**kwargs)
        print(context)#esto viene del contexto del padre
        context['pets']= Pet.objects.get(id = id)
        print(context)#esto del que nosotros creamos  context{'owners':owner} #owner = PetOwner.objects.all()
        return context

# class PetDetail(View):
#     def get(self,request,id):
#         pet = Pet.objects.get(id=id)
#         context = {"pets": pet}
#         template = loader.get_template("vet/pets/pet_detail.html")
#         return HttpResponse(template.render(context, request))



##vista como funcion
def test(request):
    print(request.__dict__)
    return HttpResponse("hello world")


##vista como clase
class Test(View):
    def get(self,request):
        #print(request.__dict__)
        return HttpResponse("hello world from class view")
