from django.shortcuts import get_object_or_404, redirect, render
from inventario.models import *
from .models import *

# Create your views here.
def venta(request):
    
    return render(request, 'Venta/venta.html')

def buscadorProducto(request):
    return render(request,'Venta/productos.html')
def caja(request):
    return render(request,'Venta/caja.html')
from django.http import JsonResponse

def agregar_producto(request):
    bar_code = request.GET.get('bar_code')
    productos = Product.objects.filter(bar_code=bar_code)
    
    data = ''
    for producto in productos:
        data += f'<tr ><td>{producto.name}</td><td>${producto.buy_price}</td><td>{producto.stock}</td><td>{producto.bar_code}</td><td><button class="btn btn-danger" onclick="eliminarFila(this)">Eliminar</button></td></tr>'
    print(bar_code)
    return JsonResponse({'data': data}, safe=False)
def reducir_stock(request):
    if request.method == 'GET':
        bar_code = request.GET.get('bar_code')
       
        
        try:
            producto = get_object_or_404(Product, bar_code=bar_code)
            producto.stock -= 1
            producto.save()
            return JsonResponse({'message': 'Stock reducido correctamente.'})
        except Product.DoesNotExist:
            return JsonResponse({'message': 'No se encontró el producto especificado.'})