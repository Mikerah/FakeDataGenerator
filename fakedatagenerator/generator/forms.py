from django import forms

class QueryForm(forms.Form):
    type = forms.ChoiceField(choices=[(1,"Regression"), (2,"Classification")], required=True)
    number_of_predictors = forms.IntegerField(max_value=20, initial=1, required=True)
    number_of_data_points = forms.IntegerField(max_value=10000, initial=100, required=True)
    file_name = forms.CharField(max_length=100, required=True)
    file_format = forms.ChoiceField(choices=[(1,"txt"),(2,"csv"), (3, "json")], required=True)