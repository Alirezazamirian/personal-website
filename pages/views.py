from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from django.views import View
from django.views.generic import ListView, DetailView
from .models import User, Education, Experience, SiteSettings, Awards, Skills, Projects, Services
from .forms import ContactMeForm
from django.contrib import messages


class Credential(View):
    def get(self, request):
        personal_info = get_context('user').get('personal_info')
        educations = get_context('education').get('education')
        experiences = get_context('experience').get('experience')
        awards = get_context('award').get('award')
        skills = get_context('skill').get('skill')
        site = get_context('site').get('site')

        context = {
            'skills': skills,
            'personal_info': personal_info,
            'experiences': experiences,
            'educations': educations,
            'awards': awards,
            'site': site
        }
        return render(request, 'pages/credentials.html', context)


class HomePage(View):
    def get(self, request):
        personal_info = get_context('user').get('personal_info')
        site = get_context('site').get('site')
        return render(request, 'pages/home.html', {'personal_info': personal_info, 'site': site})


class ContactMe(View):

    def get(self, request):
        site = get_context('site').get('site')
        form = ContactMeForm()
        return render(request, 'pages/contact.html', {'site': site, 'form': form})

    def post(self, request):
        form = ContactMeForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            context = {
                'name': user_name,
                'message': message
            }

            try:
                html_message = render_to_string('pages/mail_service/mail_template.html', context)
                plain_message = strip_tags(html_message)
                send_mail(subject, plain_message, email, ['alirezazamirian@gmail.com'], html_message=html_message)
                messages.success(request, 'Your message was sent successfully.')
            except:
                pass

            return redirect(reverse('contact_me'))
        else:
            messages.error(request, 'An error occurred.')
            return render(request, 'pages/contact.html', {'form': form})


class AboutMe(View):
    def get(self, request):
        personal_info = get_context('user').get('personal_info')
        site = get_context('site').get('site')
        experience = get_context('experience').get('experience')
        education = get_context('education').get('education')

        context = {
            'personal_info': personal_info,
            'experience': experience,
            'education': education,
            'site': site
        }
        return render(request, 'pages/about.html', context)


class ProjectsView(ListView):
    model = Projects
    template_name = 'pages/projects_list.html'
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['services'] = Services.objects.filter(is_main=False)
        print(context)
        return context
        # if object_list.count() > 2:
    # def get(self, request, *args, **kwargs):
    #     return render(request, 'pages/projects_detail.html',{})


class ProjectDetailView(DetailView):
    model = Projects
    context_object_name = 'project'
    template_name = 'pages/projects_detail.html'


class ServicesView(View):
    def get(self, request):
        site = get_context('site').get('site')
        services = Services.objects.filter(is_main=True)
        context = {
            'site': site,
            'services': services
        }
        return render(request, 'pages/services.html', context)


def get_context(name=None):
    context = None
    if name == 'user':
        user = User.objects.filter(is_active=True).first()
        context = {'personal_info': user}

    if name == 'site':
        site = SiteSettings.objects.filter(is_active=True).first()
        context = {'site': site}

    if name == 'experience':
        experience = Experience.objects.filter(is_active=True)
        context = {'experience': experience}

    if name == 'education':
        education = Education.objects.filter(is_active=True)
        context = {'education': education}

    if name == 'award':
        award = Awards.objects.filter(is_active=True)
        context = {'award': award}

    if name == 'skill':
        skill = Skills.objects.filter(is_active=True)
        context = {'skill': skill}

    return context
