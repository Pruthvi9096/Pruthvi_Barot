from django.shortcuts import render
from visitor_app.models import VisitFor,Department,Visitor,Visit
from visitor_app.forms import VisitForm,VisitorForm,VisitForForm,DepartmentForm
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import cv2
from datetime import datetime
import base64
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string,get_template
from weasyprint import HTML
from io import BytesIO
import xhtml2pdf.pisa as pisa

@login_required(login_url='/login/')
def visit_index(request):
    visit = Visit.objects.all().order_by('-pk')
    context = {
        'visit': visit
    }
    return render(request, 'visit_index.html', context)

def all_department(request):
    department = Department.objects.all()
    context = {
        'department':department
    }
    return render(request,'all_department.html',context)

def all_visitor(request):
    visitor = Visitor.objects.all()
    context = {
        'visitor':visitor
    }
    return render(request,'all_visitor.html',context)


def visit_profile(request,pk):
    visitor = Visitor.objects.filter(pk=pk)
    context = {
        'visitor':visitor[0]
    }
    return render(request,'visitor_profile.html',context)

def create_visitor(request):
    form = VisitorForm()
    context = {
        'form':form
    }
    return render(request,'create_visitor.html',context)

def create_employee(request):
    form = VisitorForm()
    context = {
        'form':form
    }
    return render(request,'create_employee.html',context)

def create_visit(request):

    form = VisitForm()
    if request.method == "POST":
        form = VisitForm(request.POST)

    context = {
    	'form':form
    }
    return render(request, "visit_create.html",context)

def save_visit(request):
    form = VisitForm()
    
    visitor = Visitor.objects.filter(pk=request.POST["name"])
    visitfor = VisitFor.objects.filter(pk=request.POST["visit_to"])
    department = Department.objects.filter(pk=request.POST["department"])
    # if not department:
    #     department = Department(
    #         department_name=request.POST["department"].department_name)
    #     department.save()
    # if not visitfor:
    #     visitfor = VisitForm(
    #         name=request.POST["visit_to"].vis,
    #         )
    #     visitfor.save()
    
    visit = Visit(
        visitor_name= visitor[0],
        visitor_email = visitor[0].email,
        visitor_phone = visitor[0].phone,
        visit_to = visitfor[0],
        department = visitfor[0].department,
        purpose = request.POST["purpose"]
    )
    visit.save()
    latest_visit = Visit.objects.all()
    context = {
        'visit':latest_visit
    }
    return HttpResponseRedirect('/visitor_app/visit')

def save_visitor(request):
    print(request.FILES['image'])
    visitor = Visitor(
        name = request.POST["name"],
        email = request.POST["email"],
        phone = request.POST["phone"],
        image = request.FILES['image']
    )
    visitor.save()
    return HttpResponseRedirect('/visitor_app/create')

def visitor_save(request):
    visitor = Visitor(
        name = request.POST["name"],
        email = request.POST["email"],
        phone = request.POST["phone"],
        image = request.FILES
    )
    visitor.save()
    return HttpResponseRedirect('/visitor_app/view_all_visitor')

def open_webcam(request):
    form = VisitorForm()
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            # cv2.imwrite(img_name, frame)
            retval,buffer = cv2.imencode(img_name,frame)
            form.fields["image"].initial = ContentFile(base64.b64encode(buffer))
            print("-------------",form.fields["image"].initial)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

    return HttpResponseRedirect('/visitor_app/create_visitor')

def add_employee(request):
    
    form = VisitForForm()
    context = {
        'form':form
    }
    return render(request,'visitfor_create.html',context)

def save_employee(request):
    department = Department.objects.filter(pk=request.POST["department"])
    visit_for = VisitFor(
        name=request.POST["name"],
        department=department[0])
    visit_for.save()
    return HttpResponseRedirect('/visitor_app/create')

def add_department(request):
    
    form = DepartmentForm()
    context = {
        'form':form
    }
    return render(request,'department_create.html',context)

def create_department(request):
    
    form = DepartmentForm()
    context = {
        'form':form
    }
    return render(request,'create_department_from_dashboard.html',context)

def save_department(request):
    department = Department(
        department_name=request.POST["name"])
    department.save()
    return HttpResponseRedirect('/visitor_app/create/')

def save_department_dashboard(request):
    department = Department(
        department_name=request.POST["name"])
    department.save()
    return HttpResponseRedirect('/visitor_app/view_all_department/')

def check_in(request,pk):
    visit = Visit.objects.get(pk=pk)
    visit.checkIn_time = datetime.now()
    visit.save()
    return HttpResponseRedirect('/visitor_app/visit')

def check_out(request,pk):
    visit = Visit.objects.get(pk=pk)
    visit.checkOut_time = datetime.now()
    visit.save()
    return HttpResponseRedirect('/visitor_app/visit')

def delete_record(request,pk):
    visit = Visit.objects.get(pk=pk)
    visit.delete()
    return HttpResponseRedirect('/visitor_app/visit')

def edit_info(request,pk):
    visitor = Visitor.objects.get(pk=pk)
    form = VisitorForm()
    form.fields['name'].initial = visitor.name
    form.fields['email'].initial = visitor.email
    form.fields['phone'].initial = visitor.phone
    form.fields['image'].initial = visitor.image
    context = {
        'form':form,
        'visitor':visitor
    }
    return render(request,'edit_visitor.html',context)

def delete_info(request,pk):
    visitor = Visitor.objects.get(pk=pk)
    visitor.delete()
    return HttpResponseRedirect('/visitor_app/view_all_visitor')

def delete_department(request,pk):
    department = Department.objects.get(pk=pk)
    department.delete()
    return HttpResponseRedirect('/visitor_app/view_all_department')


def save_info(request,pk):
    visitor = Visitor.objects.get(pk=pk)
    visitor.name = request.POST["name"]
    visitor.email = request.POST["email"]
    visitor.phone = request.POST["phone"]
    visitor.image = request.FILES
    visitor.save()
    return HttpResponseRedirect('/visitor_app/view_all_visitor')

def print_visitor_pass(request,pk):
    # visitor = Visitor.objects.get(pk=pk)
    # context = {
    #     'visitor':visitor
    # }
    # html_string = render_to_string('visitor_profile.html', context)

    # html = HTML(string=html_string)
    # html.write_pdf(target='/tmp/mypdf.pdf');

    # fs = FileSystemStorage('/tmp')
    # with fs.open('mypdf.pdf') as pdf:
    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    #     return response

    # return response
    visitor = Visitor.objects.get(pk=pk)
    context = {
        'visitor':visitor
    }
    template = get_template('visitor_pass.html')
    html = template.render(context)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)


def load_name(request):
    visitor = request.GET.get('visitor')
    phone = Visitor.objects.get(pk=visitor).phone
    email = Visitor.objects.get(pk=visitor).email
    return JsonResponse({'phone':phone,'email':email})