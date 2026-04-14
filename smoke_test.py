import cv2

img = cv2.imread("img01.jpeg")

if img is None:
    print("Erro: não foi possível carregar a imagem.")
    exit()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Teste Nativo - Escala de Cinza", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()