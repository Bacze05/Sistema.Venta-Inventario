from django.shortcuts import redirect, render
from .models import *
# Vistas renderizado de plantilla
def home(request):
    return render(request, 'gestionAdmin.html')
def inventario(request):
    return render(request, 'inventario/inventario.html')
def categorias(request):
    categories=Category.objects.all()
    return render(request, 'inventario/categorias.html',{'Category':categories})
def proveedores(request):
    proveedor=Suppliers.objects.all()
    return render(request,'inventario/proveedores.html',{'Suppliers':proveedor})
def productos(request):
    productos=Product.objects.all()
    proveedor=Suppliers.objects.all()
    categories=Category.objects.all()
    return render(request,'inventario/productos.html',{'Product':productos,'Suppliers':proveedor,'Category':categories})

# Metodos PARA Category
def registroCategorias(request):
    nombre=request.POST['textNombre']
    categories=Category.objects.create(name=nombre)
    return redirect('categorias')
def eliminarCategorias(request,id):
    categories=Category.objects.get(id=id)
    categories.delete()
    return redirect('categorias')
def editarCategorias(request,id):
    categories=Category.objects.get(id=id)
    return render(request,"inventario/editarCategorias.html",{'Category':categories})
def edicionCategorias(request):  
    id=request.POST['textId']
    nombre=request.POST['textNombre']
    categories=Category.objects.get(id=id)
    categories.name=nombre
    categories.save()
    return redirect('categorias')


# Metodos PARA Suppliers
def registroProveedores(request):
    nombre=request.POST['textNombre']
    run=request.POST['textRun']
    telefono=request.POST['textCellphone']
    email=request.POST['textEmail']
    proveedores=Suppliers.objects.create(name=nombre,run=run,cellphone=telefono,email=email)
    return redirect('proveedores')
def eliminarProveedores(request,id):
    proveedores=Suppliers.objects.get(id=id)
    proveedores.delete()
    return redirect('proveedores')
def editarProveedores(request,id):
    proveedores=Suppliers.objects.get(id=id)
    return render(request,"inventario/editarProveedores.html",{'Suppliers':proveedores})
def edicionProveedores(request):  
    id=request.POST['textId']
    nombre=request.POST['textNombre']
    run=request.POST['textRun']
    cellphone=request.POST['textCellphone']
    email=request.POST['textEmail']
    suppliers=Suppliers.objects.get(id=id)
    suppliers.name=nombre
    suppliers.run=run
    suppliers.cellphone=cellphone
    suppliers.email=email
    suppliers.save()
    return redirect('proveedores')

# Metodos PARA Productos
def registroProductos(request):
    nombre = request.POST['txtNombre']
    nombreCategoria = request.POST['txtCategoria']
    precioVenta = request.POST['txtVenta']
    precioCompra = request.POST['txtCompra']
    stock = request.POST['txtStock']
    codigoBarra = request.POST['txtBarra']
    cantidadMinima = request.POST['txtCantidad']
    nombreProveedor = request.POST['txtProveedor']
    # Busca la instancia de Category usando el nombre
    categoria = Category.objects.get(name=nombreCategoria)
    # Busca la instancia de Suppliers usando el nombre
    proveedor = Suppliers.objects.get(name=nombreProveedor)
    # Crea el producto con las instancias de categoría y proveedor
    productos = Product.objects.create(
        name=nombre,
        name_category=categoria,
        price_sold=precioVenta,
        buy_price=precioCompra,
        stock=stock,
        bar_code=codigoBarra,
        minimum_amount=cantidadMinima,
        suppliers=proveedor
    )
    return redirect('productos')





