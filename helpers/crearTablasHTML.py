def crearTabla(dataFrame,nombreTabla):

    #Aqui tengo el df version HTML y archivo HTML vacio
    archivoHTML=dataFrame.to_html()
    archivo=open(f"./tablas/{nombreTabla}.html","w",encoding='UTF-8')

    #Crear el archivo HTML
    archivo.write('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="./assets/styles/styles.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    <title>Tabla</title>
    </head>
    <body>
    ''')
    archivo.write(archivoHTML)
    archivo.write('''
    </body>
    </html>
    ''')
    #Cerrar el archivo HTML
    archivo.close()
