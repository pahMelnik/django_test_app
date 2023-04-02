from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import Form1
import polls.scripts.image_to_ascii as ita

# Create your views here.
class Page(View):
    form_class = Form1
    def get(self, request):
        context = {
            "form": self.form_class
        }
        return render(request, "image_to_ascii.html", context)
    def post(self, request):
        print(request.POST)
        context = {
            "form": self.form_class,
            "post_request":  self.image_to_ascii(request.FILES['image_path'],
                                                 request.POST['image_scale'],
                                                 request.POST['vertical_scale'],
                                                 request.POST['palette'])
        }
        return render(request, "image_to_ascii.html", context)

    def image_to_ascii(self, image, image_scale, vertical_scale, palette):
        palette = [char for char in palette]
        image_obj = ita.read_image(image, float(image_scale))
        pixels = ita.get_pixels(image_obj)
        number = ita.convert_pixels_to_number(pixels, len(palette))
        number = ita.zip_number_array(number, int(vertical_scale))
        char = ita.convert_number_to_char(number, palette)
        rows = ["".join(row) for row in char]
        return rows



