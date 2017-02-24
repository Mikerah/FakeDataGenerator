from django.shortcuts import render
from django.http import HttpResponse
from .forms import QueryForm
from .utils import generate
from io import StringIO
from . import constants

def index(request):
    if request.method == "POST":
        form = QueryForm(request.POST)
        
        if form.is_valid():
            type = constants.types[int(form.cleaned_data['type'])]
            num_predictors = int(form.cleaned_data['number_of_predictors'])
            num_data_points = int(form.cleaned_data['number_of_data_points'])
            file_name = form.cleaned_data['file_name']
            file_type = constants.file_formats[int(form.cleaned_data['file_format'])]
            
            f = generate(num_predictors,num_data_points,file_name,type,file_type)
            file_to_dl = open(f.name)
            response = HttpResponse(file_to_dl, content_type="text/"+file_type)
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_to_dl.name)
            file_to_dl.close()
            return response
    else:
        form = QueryForm()
    
    return render(request, 'generator/index.html', {'form': form})
