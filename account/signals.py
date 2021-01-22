from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
from django.contrib import messages


@receiver(user_login_failed)
def login_attempt_failure_handler(sender, request, **kwargs):
	return messages.error(request, 'کاربری با مشخصات وارد شده یافت نشد!')
