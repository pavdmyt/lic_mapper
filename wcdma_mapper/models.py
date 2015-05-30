from django.db import models


class RAitem(models.Model):
    item_code = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=128, default='Description.')

    def __unicode__(self):
        return self.item_code

    class Meta:
        verbose_name_plural = 'RA sales items'


class FeatureID(models.Model):
    ra_item = models.ForeignKey(RAitem)
    feature_id = models.CharField(max_length=20)

    def __unicode__(self):
        return self.feature_id

    class Meta:
        verbose_name_plural = 'RA features IDs'


class OSSitem(models.Model):
    # !!! TODO: ra_item = models.ForeignKey(RAitem.item_code)
    feature_id = models.ForeignKey(FeatureID)
    item_code = models.CharField(max_length=50)
    description = models.CharField(max_length=128, default='Description.')

    def __unicode__(self):
        return self.item_code

    class Meta:
        verbose_name_plural = 'OSS sales items'
