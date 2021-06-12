from contacts.models import Contact
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']

        # Check if the user has already made an inquiry
        if request.user.is_authenticated:
            has_contacted = Contact.objects.filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # send_mail(
        #     'Property Listing Inquiry',
        #     'You have an inquiry for '+listing+'.',
        #     settings.EMAIL_HOST_USER,
        #     [realtor_email],
        #     fail_silently=False
        # )

        messages.success(
            request, 'Made an inquiry successfully. Realtor will get back to you as soon as possible!')
        return redirect('/listings/'+listing_id)
