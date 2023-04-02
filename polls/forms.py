from django import forms



class Form1(forms.Form):
    image_path = forms.ImageField()
    image_scale = forms.FloatField(initial=1, required=False)
    vertical_scale = forms.IntegerField(initial=2, required=False)
    palette = forms.ChoiceField(widget=forms.RadioSelect, 
                                choices= [
                                    (".:-=+*#%@",".:-=+*#%@"),
                                    ("@$#*+=-:.","@$#*+=-:."),
                                    (".'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$",".'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"),
                                    ("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.", "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")
                                ]
                                ,required=True)
