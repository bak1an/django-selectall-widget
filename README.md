##How to use:

* Add jquery to your project (if it is not added already)
* Put __templates__ dir contents and __widgets.py__ file into your application dir
* Use: 

    from django import forms
    from myapp.widgets import CheckboxSelectMultipleWithSelectAll
    class MyForm(forms.Form):
        options = forms.MultipleChoiceField(widget=CheckboxSelectMultipleWithSelectAll, choices=[(1,"first"),(2,"second"),(3,"third")])

