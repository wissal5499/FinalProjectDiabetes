from django.utils.translation import gettext as _
from django.db import models
# Create your models here.

class survey (models.Model):
    diabetic= models.CharField(_("diabetic"), max_length=50,default="Y")
    gender=models.CharField(_("gender"), max_length=50)
    age=models.IntegerField(_("age"))
    parents=models.CharField(_("parents"), max_length=50)
    siblings=models.CharField(_("siblings"), max_length=50)
    fast_food_in_night=models.CharField(_("fast food in night"), max_length=50)
    sweet=models.CharField(_("sweet"), max_length=50)
    hypertension=models.CharField(_("hypertension"), max_length=50)
    stress=models.CharField(_("stress"), max_length=50)
    delayed_healing_wounds=models.CharField(_("delayed healing wounds"), max_length=50)
    delayed_bruise_recovery=models.CharField(_("delayed bruise recovery"), max_length=50)
    thirst=models.CharField(_("thirst"), max_length=50)
    urination=models.CharField(_("urination"), max_length=50)
    tired=models.CharField(_("tired"), max_length=50)
    blurred_vision=models.CharField(_("blurred vision"), max_length=50)
    numbness=models.CharField(_("numbness"), max_length=50)
    smoking=models.CharField(_("smoking"), max_length=50)
    sport=models.CharField(_("sport"), max_length=50)
    BMI=models.FloatField(_("BMI"))
    area=models.CharField(_("area"), max_length=50)












  