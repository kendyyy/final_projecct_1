from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class Render:

    @staticmethod
    def render(path: str, context: dict):
        template = get_template(path)
        html = template.render(context)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)
    
    @staticmethod
    def render_for_download(path: str, context: dict):
        template = get_template(path)
        html = template.render(context)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            http_response = HttpResponse(response.getvalue(), content_type='application/pdf')
            http_response['Content-Disposition'] = 'attachment; filename="formualaire.pdf"'
            return http_response
        else:
            return HttpResponse("Error Rendering PDF", status=400)