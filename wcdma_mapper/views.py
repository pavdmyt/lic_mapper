from django.shortcuts import render
from django.http import HttpResponseRedirect

from wcdma_mapper.models import RAitem, FeatureID, OSSitem
from wcdma_mapper.forms import MapForm, UploadFileForm

# Function to handle uploaded file.
from parse.xlsx_parser import get_file_data


def index(request):
    return render(request, 'wcdma_mapper/index.html')


def map_page(request, code):
    context = {}

    try:
        ra_item = RAitem.objects.get(item_code=code)
        context['ra_item'] = ra_item

        # Retrieve associated feature IDs.
        f_id = FeatureID.objects.filter(ra_item=ra_item)
        context['f_id'] = f_id

        # Retrieve associated OSS items.
        oss_item = OSSitem.objects.filter(feature_id=f_id)
        context['oss_item'] = oss_item
    except RAitem.DoesNotExist:
        pass

    return render(request, 'wcdma_mapper/map.html', context)


def map_nopage(request, code):
    context = {'ra_item': code}
    return render(request, 'wcdma_mapper/map_nopage.html', context)


def map_form(request):
    if request.method == 'POST':
        form = MapForm(request.POST)

        if form.is_valid():
            ra_item_code = form.cleaned_data.get('ra_item')
            return HttpResponseRedirect(ra_item_code + '/')

    else:
        form = MapForm()

    return render(request, 'wcdma_mapper/map_form.html', {'form': form})


def upload_file(request):
    context = {}

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():

            fname = form.cleaned_data.get('file').name
            file_data = get_file_data(request.FILES['file'], fname)
            context['file_data'] = []

            for item_code in file_data:
                try:
                    ra_item = RAitem.objects.get(item_code=item_code)

                    # Retrieve associated feature IDs.
                    f_id = FeatureID.objects.filter(ra_item=ra_item)

                    # Retrieve associated OSS items.
                    oss_item = OSSitem.objects.filter(feature_id=f_id)

                    # Fill the context.
                    context['file_data'].append({'ra_item': ra_item,
                                                 'f_id': f_id,
                                                 'oss_item': oss_item,
                                                 'code': item_code})
                except RAitem.DoesNotExist:
                    context['file_data'].append({'ra_item': None,
                                                 'f_id': None,
                                                 'oss_item': None,
                                                 'code': item_code})
            return render(request,
                          'wcdma_mapper/map_file_results.html',
                          context)

    else:
        form = UploadFileForm()

    return render(request, 'wcdma_mapper/map_file.html', {'form': form})
