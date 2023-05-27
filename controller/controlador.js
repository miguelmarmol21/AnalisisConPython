let boton = document.querySelector('#btnGenerarReporte')

boton.addEventListener('click',function(evento){
    evento.preventDefault()
    let contenedor = document.querySelector('#contenedor')
    contenedor.classList.remove('d-none')

    let nombreUsuario = document.querySelector('#nombres')
    let message = document.querySelector('#message')

    message.textContent = `Apreciado usuario ${nombreUsuario.value}, el reporte generado es: `
})