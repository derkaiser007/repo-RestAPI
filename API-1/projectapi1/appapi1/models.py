from django.db import models

# Create your models here.
class CatResult(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    cat_score = models.DecimalField(max_digits=5, decimal_places=2)
    cat_percentile = models.DecimalField(max_digits=5, decimal_places=2)

    def possibility_of_getting_IIM(self):
        if self.cat_percentile > 90.00:
            return "Highly Possible"
        elif self.cat_percentile <= 90.00 and self.cat_percentile > 80.00:
            return "Slightly Possible"
        else:
            return "Not Possible"

"""
python manage.py shell
from appapi1.models import CatResult
CatResult.objects.create(first_name='Vivek', last_name='Singh', cat_score=97.56, cat_percentile=99.42)
CatResult.objects.all()
CatResult.objects.first()
CatResult.objects.first().first_name
exit()
"""