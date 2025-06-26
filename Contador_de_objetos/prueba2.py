import cv2
import numpy as np

# Definir el diámetro real de la moneda de referencia (en cm)
real_diameter_cm = 2.78  # 28 mm = 2.8 cm
diameter_px_total = 0  # Variable para acumular los diámetros

for i in range(10):
    # Captura de la imagen desde la cámara
    cap = cv2.VideoCapture(1)  # 0 es la cámara predeterminada
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Imagen de referencia', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):  # Presiona 's' para guardar la imagen
            cv2.imwrite('referencia.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()

    # Cargar imagen de referencia
    image = cv2.imread('referencia.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Encontrar contornos
    contornos, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos = sorted(contornos, key=cv2.contourArea, reverse=True)  # Ordenar por tamaño

    # Dibujar contornos y calcular dimensiones
    for contorno in contornos[:1]:  # Tomar el más grande
        (x, y), radius = cv2.minEnclosingCircle(contorno)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(image, center, radius, (0, 255, 0), 2)

    cv2.imshow('Moneda Detectada', image)
    cv2.waitKey(500)  # Mostrar por 0.5 segundos
    cv2.destroyAllWindows() 

    # Calcular diámetro en píxeles
    diameter_px = radius * 2
    diameter_px_total += diameter_px
    print(f'Medición {i+1}: {diameter_px} px (Acumulado: {diameter_px_total} px)')

print('\nTotal acumulado de píxeles:', diameter_px_total)
#Equivalente de pixeles por cm
pixels_per_cm = diameter_px / real_diameter_cm
print(f"1 cm equivale a {pixels_per_cm:.2f} píxeles")


# Medir otro objeto en la imagen
new_object_width_px = diameter_px   # Ejemplo
real_size_cm = new_object_width_px / pixels_per_cm
print(f"El objeto mide aproximadamente {real_size_cm:.2f} cm")