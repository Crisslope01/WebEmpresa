from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def blog(request):
    posts = Post.objects.all()      
    return render(request, "blog/blog.html", {'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})
 
# posts = Post.objects.all()  de aca obtengo todos los post directamente del modelo
# {'posts':posts}) con estos datos voy a pasar los datos a la plantilla blog.html desde la base de datos
# aca filtro los post por categoria
