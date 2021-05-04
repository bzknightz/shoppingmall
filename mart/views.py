from django.shortcuts import render, redirect
from mart.models import Product
from mart.forms import ProductForm

# Create your views here.
def view_index(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("mart_index")

    products = Product.objects.all()
    context = {"form": form, "products": products}
    return render(request, "mart/index.html", context)


def view_show(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return redirect("mart_index")

    if request.GET.get("action") == "del":
        product.delete()
        return redirect("mart_index")

    if request.method == "POST" and request.GET["action"] == "edit":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_show", product.id)

    if request.GET.get("action") == "edit":
        form = ProductForm(instance=product)
        context = {"product": "product", "edit": True, "form": form}
        return render(request, "mart/show.html", context)

    context = {"product": product, "edit": False}
    return render(request, "mart/show.html", context)
