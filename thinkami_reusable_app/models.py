from django.db import models
from django import utils 

class CheckBoxItem(models.Model):
    name = models.CharField('CheckboxName', max_length=255)
    
    def __str__(self):
        return self.name
        
        
class RadioItem(models.Model):
    name = models.CharField('RadioName', max_length=255)
    
    def __str__(self):
        return self.name
        
        
class SelectItem(models.Model):
    name = models.CharField('SelectName', max_length=255)
    
    def __str__(self):
        return self.name
        
        
class SelectMultipletem(models.Model):
    name = models.CharField('SelectName', max_length=255)
    
    def __str__(self):
        return self.name
        
class FormItem(models.Model):
    registration_date = models.DateField('RegistrationDate', default=utils.timezone.now)
    pushed = models.ForeignKey(RadioItem, verbose_name='Pushed', null=True)
    checked = models.BooleanField(verbose_name='YesNo', null=False)
    checked_multiple = models.ManyToManyField(CheckBoxItem, verbose_name='CheckdMultiple')
    selected = models.ForeignKey(SelectItem, verbose_name='Selected', null=True)
    selected_multiple = models.ManyToManyField(SelectMultipletem, verbose_name='SelectedMultiple')
    input_text = models.CharField('InputText', max_length=255, blank=True)
    text_area = models.TextField('TextArea', blank=True)