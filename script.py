import qrcode

img = qrcode.make('https://binary-coffee.dev')
img_file = open('binary-coffee.png', 'wb')
img.save(img_file)
img_file.close()