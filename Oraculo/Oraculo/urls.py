"""
URL configuration for Oraculo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario import views as inventario
from venta import views as venta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inventario.home),
    path('inventario/',inventario.inventario, name='inventario'),
    path('categorias/',inventario.categorias, name='categorias'),
    path('proveedores/',inventario.proveedores,name='proveedores'),
    path('productos/',inventario.productos,name='productos'),
    path('venta/',venta.venta,name='venta'),
    path('Catalogo/',venta.buscadorProducto,name='catalogo'),
    path('caja/',venta.caja,name='caja'),


    # Links para Categorias
    path('registrarCategorias/',inventario.registroCategorias, name='registroCategoria'),
    path('editarCategory/<id>',inventario.editarCategorias, name='editarCategoria'),
    path('edicionCategory/',inventario.edicionCategorias, name='edicionCategorias'),
    path('eliminarCategory/<id>',inventario.eliminarCategorias, name='eliminarCategoria'),
    # Links para Proveedores
    path('registrarProveedor/',inventario.registroProveedores, name='registroProveedor'),
    path('editarSuppliers/<id>',inventario.editarProveedores, name='editarProveedor'),
    path('edicionSuppliers/',inventario.edicionProveedores, name='edicionProveedores'),
    path('eliminarSuppliers/<id>',inventario.eliminarProveedores, name='eliminarProveedor'),
    # Links para Productos
    path('registroProducto/',inventario.registroProductos, name='registroProducto'),

    # Links para Venta
    # path('productoVenta/',venta.btnVender, name='btnVender'),
    # path('enlistado/',venta.agregar_producto, name='agregarProducto'),
    path('venta/agregar_producto/', venta.agregar_producto, name="agregar_producto"),
    path('venta/reducir_stock/', venta.reducir_stock, name='reducir_stock'),

]

