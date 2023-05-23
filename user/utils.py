from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator


def send_password_reset_email(request, user):
    # Generate a unique token for the user
    token = default_token_generator.make_token(user)

    # Generate the reset password link
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    reset_link = f"{current_site.domain}/password-reset/confirm/{uid}/{token}/"

    # Prepare the email content
    subject = 'Password Reset Request'
    message = render_to_string('user/password_reset_email.html', {
        'user': user,
        'reset_link': reset_link,
    })
    from_email = 'your_email@example.com'  # Replace with your email address
    recipient_list = [user.email]

    # Send the email
    send_mail(subject, message, from_email,
              recipient_list, fail_silently=False)
