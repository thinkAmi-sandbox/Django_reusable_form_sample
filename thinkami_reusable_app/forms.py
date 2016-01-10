from django import forms

from .models import FormItem, RadioItem
from .widgets import DateInput

class DetailForm(forms.ModelForm):
    # ラジオボタンにて、`---------`(未選択)を表示させないように、empty_labelを設定
    pushed = forms.ModelChoiceField(
        queryset=RadioItem.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,
    )

    class Meta:
        model = FormItem
        fields = '__all__'
        widgets = {
            'registration_date': DateInput,
            'checked_multiple': forms.CheckboxSelectMultiple,
            'selected': forms.Select,   # pushedと異なり、widget指定のみは`---------`表示あり
            'selected_multiple': forms.SelectMultiple,
            'input_text': forms.TextInput,
            'text_area': forms.Textarea,
        }