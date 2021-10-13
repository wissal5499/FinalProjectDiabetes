from django.utils.translation import gettext as _
from django.db import models
# Create your models here.


class graphs (models.Model): 
    diabetic= models.CharField(_("diabetic"), max_length=50)
    type= models.CharField(_("type"), max_length=50)
    gender=models.CharField(_("gender"), max_length=50)
    age=models.IntegerField(_("age"))
    parents=models.CharField(_("parents"), max_length=50)
    siblings=models.CharField(_("siblings"), max_length=50)
    meat =models.IntegerField(_("meat"))
    carbohydrates=models.IntegerField(_("carbohydrates"))
    dairy=models.IntegerField(_("dairy"))
    fast_food_in_week=models.IntegerField(_("fast food in week"))
    fast_food_in_night=models.CharField(_("fast food in night"), max_length=50)
    nuts=models.CharField(_("nuts"), max_length=50)
    sweet=models.CharField(_("sweet"), max_length=50)
    sweetened_drinks=models.IntegerField(_("sweetened drinks"))
    hypertension=models.CharField(_("hypertension"), max_length=50)
    surgery=models.CharField(_("surgery"), max_length=50)
    stress=models.CharField(_("stress"), max_length=50)
    delayed_healing_wounds=models.CharField(_("delayed healing wounds"), max_length=50)
    delayed_bruise_recovery=models.CharField(_("delayed bruise recovery"), max_length=50)
    diseases=models.CharField(_("diseases"), max_length=50)
    healthy_food=models.CharField(_("healthy food"), max_length=50)
    thirst=models.CharField(_("thirst"), max_length=50)
    urination=models.CharField(_("urination"), max_length=50)
    infections=models.CharField(_("infections"), max_length=50)
    tired=models.CharField(_("tired"), max_length=50)
    blurred_vision=models.CharField(_("blurred vision"), max_length=50)
    numbness=models.CharField(_("numbness"), max_length=50)
    dark_colored_areas=models.CharField(_("dark colored areas"), max_length=50)
    hunger=models.CharField(_("hunger"), max_length=50)
    chew_food=models.CharField(_("chew food"), max_length=50)
    smoking=models.CharField(_("smoking"), max_length=50)
    stopped_smoking_cigarettes=models.CharField(_("stopped smoking cigarettes"), max_length=50)
    argila=models.CharField(_("argila"), max_length=50)
    sport=models.CharField(_("sport"), max_length=50)
    area=models.CharField(_("area"), max_length=50)
    Urea=models.FloatField(_("Urea"))
    Cr=models.IntegerField(_("Cr"))
    HbA1c=models.FloatField(_("HbA1c"))
    Chol=models.FloatField(_("Chol"))
    TG=models.FloatField(_("TG"))
    HDL=models.FloatField(_("HDL"))
    LDL=models.FloatField(_("LDL"))
    VLDL=models.FloatField(_("VLDL"))
    BMI=models.FloatField(_("BMI"))


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











  