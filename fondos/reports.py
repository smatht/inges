from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import HttpResponse
from django.template import Context, Template
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from io import BytesIO

from reportlab.platypus import Frame
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.platypus.para import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

stylesheet=getSampleStyleSheet()

def orden_pago_as_pdf(request, obj):
    pass