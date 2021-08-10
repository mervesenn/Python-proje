from PIL import Image

image = Image.open("23nisan.jpg")
image.save("23nisan2.jpg")
image.rotate(180).save("23nisan3.jpg")
image.rotate(90).save("23nisan4.jpg")
image.convert(mode="L").save("23nisan5.jpg")
değistir = (960, 600)
image.thumbnail(değistir)
image.save("23nisan6.jpg")
#image.filter(ImageFilter.GaussianBlur(5)).save("23nisan7.jpg")
kirpilacakalan = (340,0,950,600)
image2 = Image.open("atatürk.jpg")
image.crop(kirpilacakalan).save("23nisann.jpg")
