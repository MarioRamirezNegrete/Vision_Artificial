from PIL import Image
def RGB2Gray ():
    #conv = [0.299,0.587,0.114]
    #dat_ori = [r,g,b]
    #gray = (0.299*r)+ (0.587*g)+(0.114*b)
    imagen = Image.open("C:/Users/mario/Downloads/google.jpg")
    imagen_rgb = imagen.convert('RGB')
    ancho, alto = imagen_rgb.size # Guardamos las dimensiones de la imagen original
    imagen_gray = Image.new('L', (ancho, alto)) #Creamos una nueva imagen con las mismas dimensiones originales, L es para escala de grisesde 0 a 255

    for x in range(ancho):
        for y in range(alto):
            # Obtener el valor RGB del píxel en la posición (x, y)
            r, g, b = imagen_rgb.getpixel((x, y)) #Obtenemo valores r, g y b eb cada pixel
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)

            # Esta blecer el valor de gris en la nueva imagen
            imagen_gray.putpixel((x, y), gray)
    imagen_gray.save("C:/Users/mario/Downloads/google_gray.jpg") #Guarmaos la imagen
    imagen_gray.show() #Mostarmos la imagen
    return 

RGB2Gray()

