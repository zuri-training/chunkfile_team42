import os
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import zipfile
from django.template import loader
from .models import Documents
import pandas as pd
from os import listdir
from os.path import isfile, join
from django.conf import settings
from django.views.generic.base import TemplateView
from pathlib import Path


# Create your views here.
#@login_required(login_url='/login')
def dashboard(request):
    return render(request, "prototype/dashboard2.html")

def fileAuthen3(request):
    return render(request, 'prototype/fileAuthen3.html')
def filepage(request):
    return render(request, 'prototype/filepage.html')


def splita(request):
    if request.method == "POST":
        # this is the data in the file
        file_settings = request.FILES['selectedfile']
        # this is the file name extracted from the file and should include the file extension
        file_settings_name = file_settings.name
        # getting out the file extension from the file name
        file_ext = file_settings_name.split('.')[1]
        file_name = file_settings_name.split('.')[0]
        # this is the chunk size as provided by the user
        chunk_size = int(request.POST['chunk_row_size'])
        #file_size = Path(file_settings).stat()
        user = request.user

       # if chunk_size <= 0 or file_settings is None:
        #messages.error(request, "Fields cannot be empty!")
        # return redirect('prototype/dashboard.html')

        if file_ext in ("csv", "json"):

            if file_ext == "csv":

                data_set = pd.read_csv(file_settings, chunksize=chunk_size)
                counter = 0

                for chunk in data_set:
                    file_name = file_name + str(counter) + f'.{file_ext}'
                    file = chunk.to_csv(file_name, index=False)
                    with zipfile.ZipFile(f"media/{file_name}.zip", 'a', compression=zipfile.ZIP_DEFLATED) as zip_file:
                        zip_file.write(file_name,file)
                    os.remove(file_name)
                    counter += 1

                resulting_file = Documents.objects.create(docfile=f"{file_name}.zip", file_name=file_name, user=user)
                resulting_file.save()

                messages.info(request, "Split completed")
                return render(request, 'prototype/fileAuthen3.html')

            if file_ext == "json":
                data_set = pd.read_json(file_settings, lines = True)
                counter = 0

                for chunk in data_set:
                    file_name = file_name + str(counter) + f'.{file_ext}'
                    file = chunk.to_json(file_name, index=1, orient = 'record')
                    with zipfile.ZipFile(f"media/{file_name}.zip", 'a', compression=zipfile.ZIP_DEFLATED) as zip_file:
                        zip_file.write(file_name,file)
                    os.remove(file_name)
                    counter += 1

                resulting_file = Documents.objects.create(docfile=f"{file_name}.zip", file_name=file_name, user=user)
                resulting_file.save()

                messages.info(request, "Split completed")
                return render(request, 'prototype/fileAuthen3.html')

        messages.error(
            request, "Invalid file format, Please upload a valid csv or json file")
        return redirect('dashboard')

    return render(request, 'prototype/dashboard2.html')


#def storage(request):
    #template = loader.get_template('prototype/storage.html')
    #return HttpResponse(template.render())
    # return render(request, 'prototype/storage.html')
    #mydocuments = Document.objects.all().values()
    #template = loader.get_template('storage.html')
    # context = {
    # 'mydocuments' : mydocuments,
    # }
    # return HttpResponse(template.render(context, request))
    # return render(request, (output))

class MyFilesView(TemplateView):

    template_name = "auth3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # List of files in your MEDIA_ROOT
        media_path = settings.MEDIA_ROOT
        myfiles = [f for f in listdir(media_path) if isfile(join(media_path, f))]
        context['myfiles'] = myfiles

        return context