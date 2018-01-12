from django.shortcuts import render
from django.views import View
from .forms import NumberForm

from .number_2_words import number_to_words


class NumberToWords(View):
    def get(self, request):
        form_number = NumberForm()
        context = {
            'form_number': form_number
        }
        return render(request, 'input_number_form.html', context)

    def post(self, request):
        form_number = NumberForm(request.POST)
        if form_number.is_valid():
            number = form_number.cleaned_data['number']
            verbal_notation = number_to_words(number)
            context = {
                'number': number,
                'verbal_notation': verbal_notation,
            }
            return render(request, "result.html", context)
        else:
            form_number = NumberForm()
            context = {
                'form_number': form_number
            }
            return render(request, 'input_number_form.html', context)
