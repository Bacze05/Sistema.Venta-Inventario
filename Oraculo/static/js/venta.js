$(document).ready(function () {
    $('form').on('submit', function (event) {
        console.log("Formulario enviado");
        event.preventDefault();
        var bar_code = $('#bar_code').val();

        $.ajax({
            type: 'GET',
            url: '/venta/agregar_producto',
            data: { 'bar_code': bar_code },
            success: function (data) {
                console.log(data);
            
                $('#tabla-productos').append(data.data);  // Cambio aquí
                $('#bar_code').val('');
                            
                actualizarCalculadora();
                            
            }
        });
        
    });
   

    function restar_stock() {
        var productosProductos = $('#tabla-productos tr');
    
        productosProductos.each(function () {
            var productoCodBarra = $(this).find('td:eq(3)').text(); // Obtener el código de barras desde la cuarta celda
            var productoStock = parseInt($(this).find('td:eq(2)').text());
    
            // Aquí puedes realizar la lógica para restar el stock
            // por ejemplo, reducir el stock en 1
            productoStock = productoStock - 1;
    
            // Actualizar el valor del stock en la celda
            $(this).find('td:eq(2)').text(productoStock);
    
            // También puedes realizar la llamada AJAX para restar el stock en el servidor
            // utilizando el valor de productoCodBarra
            $.get('/venta/reducir_stock/', { bar_code: productoCodBarra }, function(data) {
                // No olvides manejar la respuesta del servidor si es necesario
                
            });
        });
    }
    // Asignar función restar_stock al botón de confirmar
    $(document).on('click', '.reducir-stock-btn', function () {
        restar_stock();
        console.log("Btn presionado");
        window.location.reload();
    });

    // Función para eliminar una fila
    function eliminarFila(button) {
        var fila = $(button).closest('tr');
        fila.remove();
        actualizarCalculadora();
    }

    // Asigna el evento onclick a los botones de eliminar
    $(document).on('click', '.btn-danger', function () {
        eliminarFila(this);
    });
    

    function actualizarCalculadora() {
        var productosProductos = $('#tabla-productos tr');
        var productosCalculadora = $('#tabla-calculadora');

        productosCalculadora.empty(); // Limpiar la tabla de la calculadora
        var productosContados = {}; // Objeto para llevar un registro de las cantidades

        productosProductos.each(function () {
            var productoNombre = $(this).find('td:eq(0)').text();
            var productoPrecio = parseFloat($(this).find('td:eq(1)').text().replace('$', ''));
            var productoStock = parseInt($(this).find('td:eq(2)').text()); // Agregar esta línea para obtener el stock
            var productoKey = productoNombre + '_' + productoPrecio; // Crear una clave única

            if (productosContados[productoKey]) {
                productosContados[productoKey].cantidad++;
            } else {
                productosContados[productoKey] = { cantidad: 1, nombre: productoNombre, precio: productoPrecio, stockOriginal: productoStock, stock: productoStock - 1 }; // Agregar el stock al objeto
            }
        });

        var totalCalculadora = 0;

        for (var productoId in productosContados) {
            var producto = productosContados[productoId];
            var productoPrecio = parseFloat(producto.precio);
            var subtotal = producto.cantidad * productoPrecio;

            var nuevaFila = `
            <tr>
            <td>${producto.nombre}</td>
            <td>${producto.cantidad}</td>
            <td>$${productoPrecio}</td>
            <td class="stock-column">${producto.stock}</td> <!-- Agregar la columna de stock -->
            <td><span id="subtotal-${productoId}">$${subtotal}</span></td>
            </tr>`;

            productosCalculadora.append(nuevaFila);
            totalCalculadora += subtotal;

            // Actualizar el subtotal en la celda correspondiente
            $('#subtotal-' + productoId).text('$' + subtotal);
        }

        // Actualizar el total mostrado en la interfaz
        $('#totalCalculadora').text('$' + totalCalculadora);
    }
});
