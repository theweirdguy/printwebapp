from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render
from .models import Receipt
# Create your views here.


def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    registration_number = request.POST['registration']
    receipt_object = Receipt.objects.get(registration_no=registration_number)

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setLineWidth(.3)

    p.setFont('Helvetica-Bold', 15)
    p.drawString(260, 800, 'Student Copy')

    p.setFont('Helvetica-Bold', 17)
    p.drawString(30, 770, receipt_object.photo_type)

    p.setFont('Helvetica-Bold', 13)
    p.drawString(30, 728, 'Registration No.')
    p.drawString(380, 728, 'Date')
    p.drawString(30, 700, 'Student Name')
    p.drawString(380, 700, 'Phone no.')
    p.drawString(30, 670, "Studio No.")
    p.drawString(230, 670, 'FileName')


    p.setFont('Helvetica', 13)
    p.drawString(150, 728, registration_number)
    p.line(150, 726, 200, 726)
    p.drawString(420, 728, receipt_object.date)
    p.line(420, 726, 489, 726)
    p.drawString(150, 700, receipt_object.student_name)
    p.line(150, 698, 150+len(receipt_object.student_name)*8.6, 698)
    p.drawString(455, 700, receipt_object.phone_number)
    p.line(455, 698, 530, 698)

    p.line(445, 690, 530, 690)
    p.line(445, 690, 445, 660)
    p.drawString(455, 670, "Rs. " + receipt_object.price + "/-")
    p.line(530, 690, 530, 660)
    p.line(445, 660, 530, 660)

    p.line(25, 640, 535, 640)

    p.setFont('Helvetica-Bold', 15)
    p.drawString(260, 610, 'Merchant Copy')

    p.setFont('Helvetica-Bold', 17)
    p.drawString(30, 580, receipt_object.photo_type)

    p.setFont('Helvetica-Bold', 13)
    p.drawString(30, 538, 'Registration No.')
    p.drawString(380, 538, 'Date')
    p.drawString(30, 510, 'Student Name')
    p.drawString(380, 510, 'Phone no.')
    p.drawString(30, 480, "Studio No.")
    p.drawString(230, 480, 'FileName')

    p.setFont('Helvetica', 13)
    p.drawString(150, 538, registration_number)
    p.line(150, 536, 200, 536)
    p.drawString(420, 538, receipt_object.date)
    p.line(420, 536, 489, 536)
    p.drawString(150, 510, receipt_object.student_name)
    p.line(150, 508, 150 + len(receipt_object.student_name) * 8.6, 508)
    p.drawString(455, 510, receipt_object.phone_number)
    p.line(455, 508, 530, 508)

    p.line(445, 500, 530, 500)
    p.line(445, 500, 445, 470)
    p.drawString(455, 480, "Rs. " + receipt_object.price + "/-")
    p.line(530, 500, 530, 470)
    p.line(445, 470, 530, 470)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    #import pdb
    receipt_object.is_printed=True
    receipt_object.save()
    #pdb.set_trace()
    return response


def data_view(request):
    context = {'printed_receipt': Receipt.objects.filter(is_printed=True)}
    return render(request, 'receipt/index.html', context)