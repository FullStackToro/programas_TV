from django.db import models
from datetime import datetime
from time import gmtime, strftime


class Libro_manager(models.Manager):
    def validacion(self, postData):
        error = {}
        time = datetime.strptime(postData['fecha_1'], '%Y-%m-%d')
        now=datetime.now()
        largo_data = [2, 3, 10]
        if len(postData['titulo_1']) < largo_data[0]:
            error['titulo_1']=f"El título debe tener {largo_data[0]} caracteres"
        if len(postData['net_1']) < largo_data[1]:
            error['net_1'] = f"El network debe tener {largo_data[1]} caracteres"
        if time > datetime.now():
            error['net_1'] = f"La fecha no puede ser superior a {now.year}/{now.month}/{now.day}"
        data=postData['desc']
        print(len(data.replace(" ","")))
        if len(data.replace(" ","")) < largo_data[2]:
            if postData['desc'] is None:
                pass
            else:
                error['desc'] = f"La descripción debe tener {largo_data[2]} caracteres"
        return error


    def validacion_new(self, postData):
        error = {}
        largo_data = [2, 3, 10]
        if len(postData['titulo_1']) < largo_data[0]:
            error['titulo_1'] = f"El título debe tener {largo_data[0]} caracteres"
        if len(postData['net_1']) < largo_data[0]:
            error['net_1'] = f"El network debe tener {largo_data[1]} caracteres"
        if len(postData['desc']) < largo_data[0]:
            if postData['desc'] is None:
                pass
            else:
                error['desc'] = f"La descripción debe tener {largo_data[2]} caracteres"
        unique_title = Libro.objects.all()
        for libro in unique_title:
            if postData['titulo_1'].lower() == libro.title.lower():
                error['title2'] = f"El nombre {libro.title} ya existe"
        return error



class Libro(models.Model):
    title = models.CharField(max_length=255)
    netword = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Libro_manager()


