from django.shortcuts import render, redirect
from .models import ProjectDetails
from .forms import ProjectDetailsCreate
from django.http import HttpResponse

#DataFlair
def index(request):
    shelf = ProjectDetails.objects.all()
    return render(request, 'project_details/index.html', {'shelf': shelf})

def upload(request):
    upload = ProjectDetailsCreate()
    if request.method == 'POST':
        upload = ProjectDetailsCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'project_details/upload_form.html', {'upload_form':upload})

def update_project_details(request, project_details_id):
    project_details_id = int(project_details_id)
    try:
        project_details_sel = ProjectDetails.objects.get(id = project_details_id)
    except ProjectDetails.DoesNotExist:
        return redirect('index')
    project_details_form = ProjectDetailsCreate(request.POST or None, instance = project_details_sel)
    if project_details_form.is_valid():
       project_details_form.save()
       return redirect('index')
    return render(request, 'project_details/upload_form.html', {'upload_form':project_details_form})

def delete_project_details(request, project_details_id):
    project_details_id = int(project_details_id)
    try:
        project_details_sel = ProjectDetails.objects.get(id = project_details_id)
    except ProjectDetails.DoesNotExist:
        return redirect('index')
    project_details_sel.delete()
    return redirect('index')
