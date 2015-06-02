import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lic_mapper.settings')

import django
django.setup()

from wcdma_mapper.models import RAitem, FeatureID, OSSitem


def populate():

    ## RU00104.T
    ra_item = add_ra_item(code='RU00XXX.T',
                          descr='RU00XXX.T description')

    feature_id = add_feature_id(ra_item=ra_item,
                                f_id='RAN00X')

    oss_item = add_oss_item(f_id=feature_id)

    ## RU00409.T
    ra_item = add_ra_item(code='RU01XXX.T',
                          descr='RU01XXX description')

    feature_id = add_feature_id(ra_item=ra_item,
                                f_id='RAN01X')

    oss_item = add_oss_item(f_id=feature_id,
                            code='OSSW01XX',
                            descr='OSSW01XX description')

    ## RU00318.T
    ra_item = add_ra_item(code='RU02XXX.T',
                          descr='RU02XXX.T description')

    feature_id1 = add_feature_id(ra_item=ra_item,
                                 f_id='RAN02X')

    feature_id2 = add_feature_id(ra_item=ra_item,
                                 f_id='RAN03X')

    oss_item1 = add_oss_item(f_id=feature_id1,
                             code='OSSW02XX',
                             descr='OSSW02XX description')

    oss_item1 = add_oss_item(f_id=feature_id2,
                             code='OSSW03XX',
                             descr='OSSW03XX description')

    # Print out added items
    for _item in RAitem.objects.all():
        for _id in FeatureID.objects.filter(ra_item=_item):
            for _oss_item in OSSitem.objects.filter(feature_id=_id):
                print("- {0} - {1} - {2}".format(str(_item),
                                                 str(_id),
                                                 str(_oss_item)))


def add_ra_item(code, descr='description'):
    item = RAitem.objects.get_or_create(item_code=code,
                                        description=descr)[0]
    return item


def add_feature_id(ra_item, f_id):
    feat = FeatureID.objects.get_or_create(ra_item=ra_item,
                                           feature_id=f_id)[0]
    return feat


def add_oss_item(f_id, code=None, descr=None):
    item = OSSitem.objects.get_or_create(feature_id=f_id)[0]

    if code:
        item.item_code = code

    if descr:
        item.description = descr

    item.save()
    return item


if __name__ == '__main__':
    print("Starting WCDMAP mapper population script...")
    populate()
