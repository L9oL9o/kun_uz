from django.shortcuts import render

def test_view(request):
    # Your view logic here
    return render(request, 'base.html')
