from tokenize import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import token
import math, random

numList = []


def listCheck(otp):
    if otp in numList:
        generateOTP()
    elif len(numList) < 100:
        numList.append(otp)
        return otp
    else:
        del numList[0]
        numList.append(otp)
        return otp


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return listCheck(OTP)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_new_user(sender, **kwargs):
    user = kwargs['instance']
    generated_otp = generateOTP()
    if kwargs['created']:
        if not(user.is_staff or user.is_superuser):
            token.objects.create(user=user, token=generated_otp)
            send_mail('OTP verification', generated_otp,
                      settings.DEFAULT_FROM_EMAIL, [user.email])


            # set the variable initially created to True
            messageSent = True
    

# def generateOTP() :
#     digits = "0123456789"
#     OTP = ""
#     for i in range(6) :
#         OTP += digits[math.floor(random.random() * 10)]
#     return OTP


