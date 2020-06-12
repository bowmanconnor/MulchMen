from twilio.rest import Client
from django.conf import settings
from django.core.mail import send_mail
from mulchmen.settings import EMAIL_HOST_USER

from datetime import datetime

def new_appointment(appointment):
    subject = 'Thank you for your interest in MulchMen'
    message = 'Hi '  + appointment.user.first_name + ',\n \nThank you for scheduling online! We have recieved your online appointment request and will be in contact shortly to confirm the details. To view your appointment details click here mulchmen.org/orders/. Thank you for your interest in MulchMen! We cannot wait to transform your yard! \n\nThanks, \n\nMulchMen \nwww.mulchmen.org \nmulchmenmail@gmail.com \n(440) 539-3348'
    recipient = appointment.user.email
    send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)


    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    DELIVERY_CHOICES = {'P' : 'I will set up the mulch delivery', 'M': 'I would like MulchMen to set up the mulch delivery'}
    delivery = DELIVERY_CHOICES[appointment.delivery]
    if appointment.weeding:
        weeding = "Weeding"
    else:
        weeding = "No Weeding"

    if appointment.bed_cleaning:
        bed_cleaning = "Bed Cleaning"
    else:
        bed_cleaning = "No Bed Cleaning"

    if appointment.edging:
        edging = "Edging"
    else:
        edging = "No Edging"

    message_to_broadcast = ("New Appointment \n"+
        "--------------- \n" +
        appointment.name + "\n" +
        str(appointment.cubic_yards) + " cubic yards\n" +
        weeding + "\n" +
        bed_cleaning + "\n" +
        edging + "\n" +
        appointment.date.strftime("%A %B %d") + "\n" +
        delivery + "\n" +
        appointment.hear_about_us + "\n" +
        appointment.additional_comments + "\n" +
        appointment.email + "\n" +
        str(appointment.phone) + "\n" +
        appointment.address + "\n\n" +
        "mulchmen.org/appointments/")
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient, from_=settings.TWILIO_NUMBER, body=message_to_broadcast)
            print("messgae sent to " + recipient)
            

def add_appointment_sms(appointment, user_who_added):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    DELIVERY_CHOICES = {'P' : 'I will set up the mulch delivery', 'M': 'I would like MulchMen to set up the mulch delivery'}
    STATUS_CHOICES = {'P' : 'Pending', 'S' : 'Scheduled', 'C' : 'Completed'}

    delivery = DELIVERY_CHOICES[appointment.delivery]
    status = STATUS_CHOICES[appointment.status]

    if appointment.weeding:
        weeding = "Weeding"
    else:
        weeding = "No Weeding"

    if appointment.bed_cleaning:
        bed_cleaning = "Bed Cleaning"
    else:
        bed_cleaning = "No Bed Cleaning"

    if appointment.edging:
        edging = "Edging"
    else:
        edging = "No Edging"

    message_to_broadcast = (user_who_added + " added an appointment\n"+
        "--------------- \n" +
        appointment.name + "\n" +
        str(appointment.cubic_yards) + " cubic yards\n" +
        status + "\n" +
        weeding + "\n" +
        bed_cleaning + "\n" +
        edging + "\n" +
        appointment.date.strftime("%A %B %d") + "\n" +
        delivery + "\n" +
        appointment.hear_about_us + "\n" +
        appointment.additional_comments + "\n" +
        appointment.email + "\n" +
        str(appointment.phone) + "\n" +
        appointment.address + "\n\n" +
        "mulchmen.org/appointments/")
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient, from_=settings.TWILIO_NUMBER, body=message_to_broadcast)


def appointment_confirmed(appointment):
    if appointment.email != "example@example.com":
        subject = 'Your order has been confirmed!'
        message = 'Hi '  + appointment.user.first_name + ',\n \nYour order has been confirmed! We cannot wait to transform your yard on ' + appointment.date.strftime("%A %B %d") +'. To view more of your appointment details click here mulchmen.org/orders/. If you have any further questions or concerns let us know. Thank you for your interest in MulchMen!\n\nThanks, \n\nMulchMen \nwww.mulchmen.org \nmulchmenmail@gmail.com \n(440) 539-3348'
        recipient = appointment.user.email
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
        
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        message_to_broadcast = ("\n"+
            appointment.name + "'s appointment was confirmed" + "\n" + 
            "mulchmen.org/appointments/")
        for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
            if recipient:
                client.messages.create(to=recipient, from_=settings.TWILIO_NUMBER, body=message_to_broadcast)

def complete_appointment_email(appointment):
    if appointment.email != "example@example.com":
        subject = 'Thank you for choosing MulchMen'
        message = 'Hi '  + appointment.user.first_name + ',\n \nThank you for choosing us for your mulching needs this year! If you are pleased with how your yard turned out, any form of recommendation is how our little business stays alive! We thrive on your Facebook posts or when you tell your neighbors about us when they inevitably ask how your yard looks so darn good. Thank you once again and we hope you keep us in mind next summer. \n\nThanks, \n\nMulchMen \nwww.mulchmen.org \nmulchmenmail@gmail.com \n(440) 539-3348'
        recipient = appointment.user.email
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)