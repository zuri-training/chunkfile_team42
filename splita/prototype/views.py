import os
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import zipfile
from django.template import loader
from .models import Document
import pandas as pd


# Create your views here.
# @login_required(login_url='/login')
def dashboard(request):
    return render(request, "prototype/dashboard2.html")


def fileAuthen(request):
    myfiles = Document.objects.all().values()
    template = loader.get_template('prototype/fileAuthen.html')
    context = {
        'myfiles': myfiles
    }
    return HttpResponse(template.render(context, request))


def splita(request):
    if request.method == "POST":
        # this is the data in the file
        file_settings = request.FILES['selectedfile']
        # this is the file name extracted from the file and should include the file extension
        file_name = file_settings.name
        # getting out the file extension from the file name
        file_ext = file_name.split('.')[1]
        file_name1 = file_name.split('.')[0]
        # this is the chunk size as provided by the user
        chunk_size = int(request.POST['chunk_row_size'])
        #user = request.user

        if file_ext in ("csv", "json"):
            data_set = pd.read_csv(file_settings, chunksize=chunk_size)
            counter = 0

            for chunk in data_set:
                file_name = file_name1 + str(counter) + f'.{file_ext}'
                file = chunk.to_csv(file_name, index=False)
                with zipfile.ZipFile(f"media/{file_name1}.zip", 'a', compression=zipfile.ZIP_DEFLATED) as zip_file:
                    zip_file.write(file_name, file)
                os.remove(file_name)
                counter += 1

            csv_file = Document.objects.create(docfile=f"{file_name}.zip")
            csv_file.save()

            messages.info(request, "Split completed")
            return render(request, 'prototype/fileAuthen3.html')

        messages.error(
            request, "Invalid file format, Please upload a valid csv or json file")
        return redirect('dashboard')

    return render(request, 'prototype/dashboard2.html')
