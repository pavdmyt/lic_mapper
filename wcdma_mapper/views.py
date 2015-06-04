from django.shortcuts import render
from django.http import HttpResponseRedirect

from wcdma_mapper.models import RAitem, FeatureID, OSSitem
from wcdma_mapper.forms import MapForm


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
