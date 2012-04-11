from django import forms
from django.template import Context
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.core.exceptions import FieldError

class CheckboxSelectMultipleWithSelectAll(forms.CheckboxSelectMultiple):

    _all_selected = False

    def render(self, *args, **kwargs):
        empty = False
        if not self.choices:
            empty = True
        has_id = kwargs and ("attrs" in kwargs) and ("id" in kwargs["attrs"])
        if not has_id:
            raise FieldError("id required")
        select_all_id = kwargs["attrs"]["id"] + "_all"
        select_all_name = args[0] + "_all"
        original = super(CheckboxSelectMultipleWithSelectAll, self).render(*args, **kwargs)
        template = get_template("widgets/MultipleSelectWithSelectAll.html")
        context = Context({"original_widget":original, 
                           "select_all_id":select_all_id, 
                           'select_all_name':select_all_name, 
                           'all_selected':self._all_selected,
                           'empty':empty})
        return mark_safe(template.render(context))

    def value_from_datadict(self, *args, **kwargs):
        original = super(CheckboxSelectMultipleWithSelectAll, self).value_from_datadict(*args, **kwargs)
        select_all_name=args[2] + "_all"
        if select_all_name in args[0]:
            self._all_selected = True
        else:
            self._all_selected = False
        return original

