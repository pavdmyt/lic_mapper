import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lic_mapper.settings')

import django
django.setup()

from wcdma_mapper.models import RAitem, FeatureID, OSSitem

# Parsed data.
from parse.xlsx_parser import ra_dct, f_id_dct


def populate():

    # RU00104.T
    ra_item = add_ra_item(code='RU00XXX.T',
                          descr='RU00XXX.T description')

    feature_id = add_feature_id(ra_item=ra_item,
                                f_id='RAN00X')

    add_oss_item(f_id=feature_id)

    # RU00409.T
    ra_item = add_ra_item(code='RU01XXX.T',
                          descr='RU01XXX description')

    feature_id = add_feature_id(ra_item=ra_item,
                                f_id='RAN01X')

    add_oss_item(f_id=feature_id,
                 code='OSSW01XX',
                 descr='OSSW01XX description')

    # RU00318.T
    ra_item = add_ra_item(code='RU02XXX.T',
                          descr='RU02XXX.T description')

    feature_id1 = add_feature_id(ra_item=ra_item,
                                 f_id='RAN02X')

    feature_id2 = add_feature_id(ra_item=ra_item,
                                 f_id='RAN03X')

    add_oss_item(f_id=feature_id1,
                 code='OSSW02XX',
                 descr='OSSW02XX description')

    add_oss_item(f_id=feature_id2,
                 code='OSSW03XX',
                 descr='OSSW03XX description')

    # Print out added items
    for _item in RAitem.objects.all():
        for _id in FeatureID.objects.filter(ra_item=_item):
            for _oss_item in OSSitem.objects.filter(feature_id=_id):
                print("- {0} - {1} - {2}".format(str(_item),
                                                 str(_id),
                                                 str(_oss_item)))


def populate_with_parsed_data():

    # RA items
    for item in ra_dct.keys():

        ra_item = add_ra_item(code=item.get_code(),
                              descr=item.get_description())

        # Feature IDs
        for feat_id in ra_dct[item]:

            feature_id = add_feature_id(ra_item=ra_item,
                                        f_id=feat_id.get_code())

            # OSS items
            oss_items = f_id_dct.get(feat_id)

            if oss_items:
                for oss_item in f_id_dct[feat_id]:
                    add_oss_item(f_id=feature_id,
                                 code=oss_item.get_code(),
                                 descr=oss_item.get_description())
            # No OSS items found for given Feature ID
            else:
                add_oss_item(f_id=feature_id)

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
    print("Starting WCDMA mapper population script...")
    # populate()
    populate_with_parsed_data()
