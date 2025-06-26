import cv2
import numpy as np

# Definir el diámetro real de la moneda de referencia (en cm)
real_diameter_cm = 2.78
diameter_px_total = 0
diametros = []

# Tomar 10 medidas
for _ in range(10):
    # Captura de imagen
    cap = cv2.VideoCapture(1)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Imagen de referencia', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('referencia.jpg', frame)
            break

    cap.release()
    cv2.destroyAllWindows()

    # Procesamiento
    image = cv2.imread('referencia.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contornos, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos = sorted(contornos, key=cv2.contourArea, reverse=True)

    for contorno in contornos[:1]:
        (x, y), radius = cv2.minEnclosingCircle(contorno)
        diameter_px = int(radius) * 2
        diameter_px_total += diameter_px
        diametros.append(diameter_px)
        
        cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 2)
    
    cv2.imshow('Moneda Detectada', image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    print(f'Diámetro: {diameter_px} px (Total: {diameter_px_total} px)')

# Foto adicional final
print("\nPresiona 's' para tomar una foto adicional final")
cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Foto adicional final - Presiona "s"', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('referencia_final.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()

# Procesar foto final
image = cv2.imread('referencia_final.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

contornos, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos = sorted(contornos, key=cv2.contourArea, reverse=True)

for contorno in contornos[:1]:
    (x, y), radius = cv2.minEnclosingCircle(contorno)
    diameter_final = int(radius) * 2
    diametros.append(diameter_final)
    
    cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 2)

cv2.imshow('Moneda Detectada (Final)', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('\n--- Resultados finales ---')
print(f'Diámetros medidos: {diametros}')
print(f'Diámetro adicional final: {diameter_final} px')