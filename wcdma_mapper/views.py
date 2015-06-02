from django.shortcuts import render
from wcdma_mapper.models import RAitem, FeatureID, OSSitem


def index(request):
    return render(request, 'wcdma_mapper/index.html')


def map_page(request, ra_item_input):
    context = {}

    try:
        ra_item = RAitem.objects.get(item_code=ra_item_input)
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
