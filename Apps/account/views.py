from django.views.generic import FormView,View
from account.forms import LoginForm
from django.core.mail import send_mail
from django.conf import settings
from mimetypes import MimeTypes
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView
from django.http import HttpResponse
import pdfcrowd
from django.shortcuts import render,render_to_response
from pyPdf import PdfFileWriter, PdfFileReader
from account.models import Employe



class LoginView(FormView):
    '''Base class for Login'''
    form_class = LoginForm
    template_name = "login.html"


    
    def get(self, request, *args, **kwargs):
        '''
        returns Index Page with Login Form for unauthenicated user
        where as  authenticated user are returned to maps
         '''
        # if request.user.is_authenticated():
        # return  HttpResponseRedirect('/dashboard')
        context = {'form':self.form_class()}
        return self.render_to_response(context)

    
    def post(self, request, *args, **kwargs):
        '''
        authentication is done here after givings username and password
        if user is authenticated returned to maps page
        where as unauthenticated user or invalid email
        or passwords are turned back to index page with
        validation errors or invalid user
        '''
        data = request.POST.copy()
        form = self.form_class(data)
        context = {}
        # if form.is_valid():
        email = form['email']
        password = form['password']
        #     try:
        #         user = authenticate(username=email,password=password)

        #         if user is not None:
        #             login(request,user)
        #             next = request.GET.get('next', None)
        #             if next:
        #                 return HttpResponseRedirect(next)
        #             return  HttpResponseRedirect('/dashboard')
        #         else:
        #             context['message'] = 'Invalid Username or Password'
        #             context['form']= form
        #             return self.render_to_response(context)
        #     except User.DoesNotExist:
        #         context['message']='Invalid Username or Password'
        #         context['form']= form
        #         return self.render_to_response(context)
        # send_mail('welcome',[password], 'nadiya@trialx.com', [email])
        # send_mail('welcome', 'hello', settings.DEFAULT_FROM_EMAIL, [email])
        

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        subject, from_email, to = 'hello', settings.DEFAULT_FROM_EMAIL, 'nadiya@trialx.com'
        text_content = 'This is an important message.'
        html_content = '<p>This is an <strong>important</strong> message.</p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_file('/home/nadiya/Actual Diagram.jpg')

        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # context['form']= form

        # return self.render_to_response(context)


# class HighView(TemplateView):
#         template_name = "highcharts.html"



# def PdfView(request):
#     # using pdfcrowd
#     # # def pdfv(request):
#     #     template_name = "pdf.html"
#     #     try:
    #         # create an API client instance

    #         output = PdfFileWriter()



    #         client = pdfcrowd.Client("nadiya", "f0eeeebf75e3ec7fb914fc583a1160b3")


    #         # convert a web page and store the generated PDF to a variable
    #         # pdf = client.convertURI("http://www.google.com")
    #         client.setPageWidth("8.5in")
    #         client.setPageHeight("11in") 
    #         # client.setHeaderUrl("http://pdfcrowd.com{{ site.url }}/random/footer.html")
    #         # client.setFooterUrl("http://pdfcrowd.com{{ site.url }}/random/header.html")
    #         client.setHeaderHtml('<div> Hello</div>')
    #         client.setFooterHtml('<table> Foooter </table>')
    #         # pdf = client.convertURI('http://pdfcrowd.com/static/misc/lorem.html')
    #         pdf=client.convertURI('http://pdfcrowd.com/static/misc/lorem.html')
    #         input1 = PdfFileReader(file('/home/nadiya/Backups/task_tracker/html.pdf', "rb"))
    #         input1.addPage(pdf)
    #         outputStream = file("document-input1.pdf", "wb")
    #         output.write(outputStream)
    #         outputStream.close()
    #         print 'hehehehehhe'
    #     #     # print pdf
    #     #     #  # set HTTP response headers
    #         response = HttpResponse(mimetype="application/pdf")
    #         response["Cache-Control"] = "no-cache"
    #         response["Accept-Ranges"] = "none"
    #         response["Content-Disposition"] = "attachment; filename=google_com.pdf"

    #     #     # send the generated PDF
    #         response.write(pdf)

    #         return render(request,'pdf.html',{'pdf':pdf,})
    #     except pdfcrowd.Error, why:
    #         response = HttpResponse(mimetype="text/plain")
    #         response.write(why)
    #     return response

    # using pisa

# import cStringIO as StringIO
# import ho.pisa as pisa
# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse
# from cgi import escape


# def render_to_pdf(template_src, context_dict):
    
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html  = template.render(context)
#     result = StringIO.StringIO()

#     pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
#     response =  render_to_response("mytemplate.html",{'mylist':result,'pagesize':'A4'})

#     if not pdf.err:
#         return HttpResponse(result.getvalue(), mimetype='application/pdf')
#     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

# def PdfView(request):
#     result="http:www.gmail.com"

#     return render_to_pdf(
#             'mytemplate.html',
#             {
#                 'pagesize':'A4',
#                 'mylist': result,
                  # 'name':'yaseen'
#             }
#         )




                # if tipo == ".pdf":
                #     result = StringIO.StringIO()
                #     pisa.CreatePDF(unicode(response.content,encoding="utf-8"), result)
                #     return HttpResponse(result.getvalue(), mimetype='application/pdf')
                # return response

import StringIO
from cgi import escape
import xhtml2pdf.pisa as pisa
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

class PDFTemplateResponse(TemplateResponse):
    from reportlab.pdfgen import canvas
    from django.http import HttpResponse
    print "class"
    

    def generate_pdf(self, retval):
        print "gen"
        html = self.content
        # print html
        print 'lala'

        result = StringIO.StringIO()
        # rendering = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
        rendering = pisa.CreatePDF(html, result)
        print "START OF PDF"
        f=open('testxml2pdf.pdf','w')
        f.write(result.getvalue())


        print "END OF PDF"
        if rendering.err:
            return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
        else:
            self.content = result.getvalue()


    def __init__(self, *args, **kwargs):
        # print "init"
        super(PDFTemplateResponse, self).__init__(*args, mimetype='application/pdf', **kwargs)
        self.add_post_render_callback(self.generate_pdf)


class PdfView(TemplateView):
    print "view"
    response_class = PDFTemplateResponse


# class PdfView(PDFTemplateView):
#     template_name = 'mytemplate.html'



# ////////////////////////////using xhtml2pdf/////////////////////////


# import os
# from django.conf import settings
# from django.http import HttpResponse
# from django.template import Context
# from django.template.loader import get_template

# # Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
# def link_callback(uri, rel):
#     # use short variable names
#     sUrl = settings.STATIC_URL      # Typically /static/
#     sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
#     mUrl = settings.MEDIA_URL       # Typically /static/media/
#     mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

#     # convert URIs to absolute system paths
#     if uri.startswith(mUrl):
#         path = os.path.join(mRoot, uri.replace(mUrl, ""))
#     elif uri.startswith(sUrl):
#         path = os.path.join(sRoot, uri.replace(sUrl, ""))

#     # make sure that file exists
#     if not os.path.isfile(path):
#             raise Exception(
#                     'media URI must start with %s or %s' % \
#                     (sUrl, mUrl))
#     return path

# def generate_pdf(request, type):
#     # Prepare context
#     data = {}
#     data['today'] = datetime.date.today()
#     data['farmer'] = 'Old MacDonald'
#     data['animals'] = [('Cow', 'Moo'), ('Goat', 'Baa'), ('Pig', 'Oink')]

#     # Render html content through html template with context
#     template = get_template('mytemplate.html')
#     html  = template.render(Context(data))

#     # Write PDF to file
#     file = open(os.join(settings.MEDIA_ROOT, 'test.pdf'), "w+b")
#     pisaStatus = pisa.CreatePDF(html, dest=file,
#             link_callback = link_callback)

#     # Return PDF document through a Django HTTP response
#     file.seek(0)
#     pdf = file.read()
#     file.close()            # Don't forget to close the file handle
#     return HttpResponse(pdf, mimetype='application/pdf')


# 2nd method

import StringIO
import os

from cgi import escape
from xhtml2pdf import pisa 

from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template

from models import Employe


def view_in_pdf(request): 
    context_dict = {
        'object_lists': Employe.objects.all(), 
    }
    context_dict.update({'pagesize': 'Portrait'})


    template_name = "pdff.html"
    template = get_template(template_name)
    context = Context(context_dict)
    html = template.render(context)   
    result = StringIO.StringIO()
    
    pisa.CreatePDF(html.encode("UTF-8"), result , encoding='UTF-8',
                   link_callback=fetch_resources)
                   
    try:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
        
        """ for generating a new file """
        #response['Content-Disposition'] = 'attachment; filename=output.pdf'
        #return response
    except:
        return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


def fetch_resources(uri, rel):
    """ Access files and images."""
    path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    return path

def view_in_html(request):
    template_name = "pdff.html"
    object_list= Employe.objects.all()
    return render_to_response("pdff.html",{'object_lists':object_list})
# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

# def hello_pdf(request):
    #         # Create the HttpResponse object with the appropriate PDF headers.
    #     response = HttpResponse(mimetype='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    #             # Create the PDF object, using the response object as its "file."
    #     p= canvas.Canvas(response)

    #             # Draw things on the PDF. Here's where the PDF generation happens.
    #             # See the ReportLab documentation for the full list of functionality.
    #     p.drawString(100, 100, "Hello world.")

    #             # Close the PDF object cleanly, and we're done.
    #     p.showPage()
    #     p.save()
    #     return response


        # import pyPdf
        # pdf = pyPdf.PdfFileReader(open(self.hello_pdf(), "rb"))
        # for page in pdf.pages:
        #     print page.extractText()

        

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!using report lab!!!!!!!!!!!!!!!!!!!!!!!!!!1





# from reportlab.platypus.doctemplate import SimpleDocTemplate
# from reportlab.platypus import Paragraph, Spacer
# from reportlab.lib.units import inch

# # from reportlab.lib import sytles

# def PdfView(View):
#     x = Employe()
#     x.name = 'nadiya'
#     x.addr = 'harwan'
#     x.save()
#     doc = SimpleDocTemplate("products.pdf")
#     Catalog = ['hello']
#     # # header = Paragraph("Product Inventory")
#     # # Catalog.append(header)
#     # # style = styles['Normal']
#     # for product in Employe.objects.all():
#     #  # for product in Employe.objects.all():
#     #   # p = Paragraph("%s" % product.name)
#     #   Catalog.append("hello")
#     s = Spacer(1, 0.25*inch)
#     Catalog.append(s)
#     doc.build(Catalog)

#  