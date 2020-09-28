from django.db import models

# Create your models here.


class Yazar(models.Model):
    adi = models.CharField(max_length = 200)
    tc_kimlik_no = models.CharField(max_length = 11)
    
    def __str__(self):
        msg = f"{self.adi} - {self.tc_kimlik_no}"
        return msg

class Kitap(models.Model):
    adi = models.CharField(max_length = 200)
    yili = models.DateField(auto_now = True)
    notlar = models.TextField(blank=True, null= True)
    yazar  = models.ForeignKey(Yazar, on_delete = models.CASCADE)

    def __str__(self):
        msg = f"{self.adi} - {self.yili} - {self.notlar}"
        return msg
