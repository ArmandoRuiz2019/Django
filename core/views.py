from django.shortcuts import render, redirect
from .models import cursos, comentariosalumnos, portafolio, personal, experiencia, temario
from .forms import ContactoCurso
import os
from django.conf import settings
from django.http import HttpResponseRedirect, Http404, FileResponse


def confirmacionenvio(request):
    template_name = "envioemail.html"
    return render(request, template_name)


# Create your views here.
def index(request):
    template_name = "index.html"
    Cursos = cursos.objects.all()
    Comentarios = comentariosalumnos.objects.all()
    Portafolio = portafolio.objects.all()
    Personal = personal.objects.get(id=1)
    Experiencia = experiencia.objects.all()

    context = {}
    if request.method == 'POST':
        form = ContactoCurso(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(Cursos)
            form = ContactoCurso()
            return redirect(confirmacionenvio)
    else:
        form = ContactoCurso()
    context['form'] = form
    context['cursos'] = Cursos
    context['comentarios'] = Comentarios
    context['portafolio'] = Portafolio
    context['personal'] = Personal
    context['experiencia'] = Experiencia
    return render(request, template_name, context)


def vertemario(request, id):
    template_name = "temario.html"
    Temario = temario.objects.filter(curso_id=id)
    curso = cursos.objects.get(id=id)
    context = {'temario': Temario, 'curso': curso}
    return render(request, template_name, context)
