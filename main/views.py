from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Skill, Project, Experience, Achievement, ContactMessage

def index(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all().order_by('order')
    experiences = Experience.objects.all().order_by('order')
    achievements = Achievement.objects.all().order_by('order')

    # Category-wise skills filter
    languages = skills.filter(category='languages')
    frameworks = skills.filter(category='frameworks')
    tools = skills.filter(category='tools')
    core_skills = skills.filter(category='core')

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip() or 'No Subject'
        message_text = request.POST.get('message', '').strip()

        if name and email and message_text:
            # 1. Database me store karein
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text
            )

            # 2. Email alert (agar settings me password set ho)
            try:
                mail_body = f"From: {name} <{email}>\nSubject: {subject}\n\nMessage Payload:\n{message_text}"
                send_mail(
                    subject=f"Portfolio Lead: {subject}",
                    message=mail_body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['mformusa11@gmail.com'],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Email Dispatch Warning: {e}")

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/#contact')
        else:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('/#contact')

    context = {
        'profile': profile,
        'languages': languages,
        'frameworks': frameworks,
        'tools': tools,
        'core_skills': core_skills,
        'projects': projects,
        'experiences': experiences,
        'achievements': achievements,
    }
    return render(request, 'index.html', context)