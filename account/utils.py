from django.core.mail import send_mail


def send_welcome_email(email):
    url = 'http://localhost:8000/'
    message = f'<h1>Thanks for registration on our site PyShop12:</h1> {url}'
    send_mail(
        'Pyshop12 Welcome!',
        message,
        'ahalaimahalai@gmail.com',
        [email],
        fail_silently=False
    )