function checkoutSubmitDetail() {
    const producto = JSON.parse(document.getElementById('data-product-serialize-detail').value);
    const cantidad = document.getElementById('cantidad-' + producto.id + '')
    const cantidad_cajas = document.getElementById('cantidad_cajas-' + producto.id + '')
    const cantidad_xmayor = document.getElementById('cantidad_xmayor-' + producto.id + '')
    const especificaciones = document.getElementById('especificaciones-' + producto.id + '')
    producto.especificaciones = ""
    producto.cantidad = 0
    producto.cantidad_cajas = 0
    producto.cantidad_xmayor = 0

    if (producto.descuento_principal && producto.descuento_principal > 0) {
        if (producto.descuento_unidad > 0) {
            producto.total_precio = producto.descuento_unidad
        } else {
            producto.total_precio = producto.costo
        }
        producto.costo = producto.total_precio

        if (producto.descuento_mayor > 0) {
            producto.total_precio_xmayor = producto.descuento_mayor
        } else {
            producto.total_precio_xmayor = producto.costo_farsali

        }
        producto.costo_farsali = producto.total_precio_xmayor

        if (producto.descuento_caja > 0) {
            producto.total_precio_caja = producto.descuento_caja
        } else {
            producto.total_precio_caja = producto.costo_adicional
        }
        producto.costo_adicional = producto.total_precio_caja

    } else {
        producto.total_precio = producto.costo
        producto.total_precio_caja = producto.costo_adicional
        producto.total_precio_xmayor = producto.costo_farsali
    }

    if ((cantidad && cantidad.value > 0) || (cantidad_cajas && cantidad_cajas.value > 0) || (cantidad_xmayor && cantidad_xmayor.value > 0)) {
        if (especificaciones) {
            producto.especificaciones = especificaciones.value
        }
        if (cantidad && cantidad.value) {
            producto.cantidad = cantidad.value
            producto.total_precio = producto.total_precio * producto.cantidad
        }
        if (cantidad_cajas && cantidad_cajas.value) {
            producto.cantidad_cajas = cantidad_cajas.value
            producto.total_precio_caja = producto.total_precio_caja * producto.cantidad_cajas
        }
        if (cantidad_xmayor && cantidad_xmayor.value) {
            producto.cantidad_xmayor = cantidad_xmayor.value
            producto.total_precio_xmayor = producto.total_precio_xmayor * producto.cantidad_xmayor
        }
        data = []
        data.push({
            "titulo": producto.descripcion,
            "descripcion_prefer": producto.descripcion_prefer,
            "descripcion_no_prefer": producto.descripcion_no_prefer,
            "descripcion_adicional": producto.descripcion_adicional,
            "cantidad": producto.cantidad,
            "precio": producto.costo,
            "cantidad_cajas": producto.cantidad_cajas,
            "precio_caja": producto.costo_adicional,
            "cantidad_xmayor": producto.cantidad_xmayor,
            "precio_xmayor": producto.costo_farsali,
            "especificaciones": producto.especificaciones,
            "id": producto.id
        })
        // Enviamos el producto seleccionado al checkout
        // Should be triggered on form submit
        localStorage.removeItem('productos_detail')
        localStorage.setItem('productos_detail', JSON.stringify(data));
        data_productos = document.getElementById('productos-checkout-detail');
        data_productos.value = JSON.stringify(data)
        // You must return false to prevent the default form behavior
        document.getElementById('form-detail-products').submit();
        return true;
    }
    else {
        alert("Debe ingresar algun valor para hacer una compra")
        return false;
    }
}


function checkoutSubmitButtons(option) {
    data_productos = []
    form_id = null
    if (option == "1") {
        form_id = document.getElementById('form-checkout-up');
        data_productos = document.getElementById('productos-payment-1');
    } else {
        form_id = document.getElementById('form-checkout-down');
        data_productos = document.getElementById('productos-payment-2');
    }
    data_productos.value = JSON.stringify(sendProductDetail())
    form_id.submit();
    return true;
}

function sendProductDetail() {
    data = []
    productosLS = JSON.parse(localStorage.getItem('productos_detail'));
    if (productosLS && productosLS.length) {
        productosLS.forEach(function (producto) {
            data.push({
                "titulo": producto.titulo,
                "descripcion_prefer": producto.descripcion_prefer,
                "descripcion_no_prefer": producto.descripcion_no_prefer,
                "descripcion_adicional": producto.descripcion_adicional,
                "cantidad": producto.cantidad ? producto.cantidad : 0,
                "precio": producto.precio ? producto.precio : 0,
                "cantidad_cajas": producto.cantidad_cajas ? producto.cantidad_cajas : 0,
                "precio_caja": producto.precio_caja ? producto.precio_caja : 0,
                "cantidad_xmayor": producto.cantidad_xmayor ? producto.cantidad_xmayor : 0,
                "precio_xmayor": producto.precio_xmayor ? producto.precio_xmayor : 0,
                "especificaciones": producto.especificaciones,
                "id": producto.id
            })
        })
    }

    return data
}