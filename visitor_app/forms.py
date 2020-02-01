from django import forms
from visitor_app.models import *

class VisitForm(forms.Form):

    name = forms.ModelChoiceField(queryset=Visitor.objects.all(),empty_label="Choose Visitor",widget=forms.Select(
        attrs={
            "class":"custom-select mr-sm-2",
            "style":"width:90%;",
            # "onchange":"myFunction()",
        }))
        
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Phone"
        })
    )
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email"
        })
    )
    visit_to = forms.ModelChoiceField(queryset=VisitFor.objects.all(),empty_label="Visit For",widget=forms.Select(
        attrs={
            "class":"custom-select mr-sm-2",
            "style":"width:90%;"
        }))
    department = forms.ModelChoiceField(queryset=Department.objects.all(),empty_label="Choose Department",widget=forms.Select(
        attrs={
            "class":"custom-select mr-sm-2",
            "style":"width:90%;"
        }))
    purpose = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "purpose"
        })
    )

    # def clean(self):
    #     # visit = super(VisitForm, self).save(commit=False)
    #     print("-----")
    #     visitor = Visitor(name=self.cleaned_data['name'])
    #     visitor.save()
    #     visit.visitor_email = visitor.email
    #     visit.visitor_phone = visitor.phone
    #     if commit:
    #         visit.save()
    #     return visit    

class VisitorForm(forms.Form):
    # class Meta:
    #     model = Visitor
    #     fields = [
    #         'name',
    #         'phone',
    #         'email',
    #         'image'
    #     ]

    name = forms.CharField(widget=forms.TextInput(
        attrs={
        "class":"form-control",
        "placeholder":"Name"
        })
    )
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
        "class":"form-control",
        "placeholder":"Phone"
        })
    )
    email = forms.CharField(widget=forms.TextInput(
        attrs={
        "class":"form-control",
        "placeholder":"Email"
        })
    )
    image = forms.FileField()
    
class VisitForForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
        "class":"form-control",
        "placeholder":"Name"
        })
    )
    department = forms.ModelChoiceField(queryset=Department.objects.all(),empty_label="Choose Department",widget=forms.Select(
        attrs={
            "class":"custom-select mr-sm-2",
            "style":"width:90%;"
        }))

class DepartmentForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
        "class":"form-control",
        "placeholder":"Department Name"
        })
    )
