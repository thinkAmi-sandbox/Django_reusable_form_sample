from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse

from .forms import DetailForm
from .models import FormItem

# 登録時
class RegisterFormView(CreateView):
    template_name = 'form.html'
    form_class = DetailForm
	
    def get_success_url(self):
        return reverse('myform:upd', args=(self.object.id,))

# 更新時	
class UpdateFormView(UpdateView):
    model = FormItem
    template_name = 'form.html'
    form_class = DetailForm
	
    def get_success_url(self):
        return reverse('myform:upd', args=(self.object.id,))