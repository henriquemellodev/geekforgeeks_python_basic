import pyscreenshot

image = pyscreenshot.grab()

# Capturar partes de uma imagem
# image = pyscreenshot.grab(bbox=(10,10,500,500))
image.show()

image.save("MinhaTela.png")