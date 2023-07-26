
from django.core.mail import send_mail

def send_confirmation_email(email, code):
    send_mail(
        'Здравствуйте aктивируйте ваш аккаунт!',
        f'Что бы активировать ваш аккаунт нажмите на ссылку:'
        f'\n{code}'
        f'\nне передавайте его никому',
        'akusevtimur733@gmail.com',
        [email],
        fail_silently=False
    )
