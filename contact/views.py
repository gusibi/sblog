from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponse
from django.core.mail import send_mail
from contact.forms import ContactForm


def contact(request):
    errors = []
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject!')
        if not request.POST.get('message', ''):
            errors.append('Enter a message!')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a vaild e-mail address!')

        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'tuurel.server@gmail.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact.html', {
            'errors': errors,
            'subject': request.POST.get('subject', ''),
            'message': request.POST.get('message', ''),
            'email': request.POST.get('email', ''),
            }, context_instance=RequestContext(request))


def thanks(request):
    return HttpResponse('thanks')


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'tuurel.server@tuurel.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render_to_response('contact_form.html', {'form': form}, context_instance=RequestContext(request))
