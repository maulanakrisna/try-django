# from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm

from .models import Product
# Create your views here.


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj,
    }
    return render(request, "products/product_delete.html", context)


def product_update_view(request, id):
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
        return redirect('../../')
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        return redirect('../../')
    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)


def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html", context)
