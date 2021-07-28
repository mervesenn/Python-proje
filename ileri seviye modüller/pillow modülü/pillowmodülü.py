from PIL import Image

image = Image.open("23nisan.jpg")
image.save("23nisan2.jpg")
image.rotate(180).save("23nisan3.jpg")
image.rotate(90).save("23nisan4.jpg")
image.convert(mode="L").save("23nisan5.jpg")
değiştir = (960, 600)
image.thumbnail(değiştir)
image.save("23nisan6.jpg")
#image.filter(ImageFilter.GaussianBlur(5)).save("23nisan7.jpg")
kırpılacakalan = (340,0,950,600)
image2 = Image.open("atatürk.jpg")
image.crop(kırpılacakalan).save("23nisann.jpg")
