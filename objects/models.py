from django.db import models

class ObjectType(models.Model):
    name = models.CharField('Тип объекта', max_length=160)

    class Meta:
      verbose_name = 'Тип объектов'
      verbose_name_plural = 'Типы объектов'
  
    def __str__(self):
      return u'{0}'.format(self.name)

class Object(models.Model):
    name = models.CharField('Наименование объекта', max_length=160)
    object_type = models.ForeignKey(ObjectType, on_delete=models.CASCADE)
    object_address = models.CharField('Адрес объекта', max_length=160, blank=False, default=0)
    plan = models.FileField(upload_to='uploads/plans/', null=True, blank=True)
    boilers = models.IntegerField('Кол-во котлов', blank=True)
    power = models.FloatField('Мощность', blank=True)
    pumps = models.IntegerField('Кол-во насосов', blank=True)
    faucet = models.BooleanField('Наличие запорной арматуры', default=False)
    meters = models.IntegerField('Площадь', blank=True)
    people = models.IntegerField('Кол-во людей', blank=True)
    location = models.CharField('Местоположение', max_length=160)
    # connect_objects = models.ManyToManyField('self', through="Pipe")

    class Meta:
      verbose_name = 'Объект'
      verbose_name_plural = 'Объекты'
  
    def __str__(self):
      return u'{0}'.format(self.name)

class CustomerType(models.Model):
    name = models.CharField('Тип потребилетя',max_length=160)

    class Meta:
      verbose_name = 'Тип потребитей'
      verbose_name_plural = 'Типы потребителей'
  
    def __str__(self):
      return u'{0}'.format(self.name)

class Customer(models.Model):
    name = models.CharField('Наименование потребилетя',max_length=160)
    customer_type = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    customer_address = models.CharField('Адрес потребителя',max_length=160, blank=False, default=0)
    power = models.FloatField('Мощность', blank=True)
    heat_supply = models.BooleanField('Наличие отопления', default=False)
    hot_water = models.BooleanField('Наличие ГВС', default=False)
    people = models.IntegerField('Кол-во абонентов', blank=True)
    location = models.CharField('Местоположение', max_length=160)

    class Meta:
      verbose_name = 'Потребитель'
      verbose_name_plural = 'Потребители'
  
    def __str__(self):
      return u'{0}'.format(self.name)

# class Pipe(models.Model):
#     start_location = models.CharField('Местоположение начала',max_length=160)
#     destination_location = models.CharField('Местоположение окончания',max_length=160)
#     diameter = models.IntegerField('Диаметр', default=0)
#     start_object = models.ForeignKey(Object, on_delete=models.CASCADE)
#     destination_object = models.ForeignKey(Object, on_delete=models.CASCADE)

#     class Meta:
#       verbose_name = 'Труба'
#       verbose_name_plural = 'Трубы'
  
#     def __str__(self):
#       return u'{0}'.format(self.name)