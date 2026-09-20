from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject=f"New message from {name}",
            message=f"""
Name: {name}
Email: {email}

Message:
{message}
""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["franklinemmbaya@gmail.com"],
            fail_silently=False,
        )

        return render(
            request,
            "core/home.html",
            {"success": "Your message has been sent successfully!"}
        )

    return render(request, "core/home.html")