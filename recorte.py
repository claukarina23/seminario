from PIL import Image
a=('126CD_CRC-Prim-HE-02_009.tif_Row_1_Col_1')
img = Image.open(r'C:/Users/clauk/Desktop/Imagenes/0 - copia/'+a+'.tif')
#1280X768
#(izquierda,arriba,derecha,abajo)
region = (0,0,50,50)
imagen_recortada = img.crop(region)
#imagen_recortada.show()
imagen_recortada.save(r'C:\Users\clauk\Desktop\Imagenes\0-copia recortada/'+a+'_1.tif')

region = (50,0,100,50)
imagen_recortada = img.crop(region)
#imagen_recortada.show()
imagen_recortada.save(r'C:\Users\clauk\Desktop\Imagenes\0-copia recortada/'+a+'_2.tif')

region = (100,0,150,50)
imagen_recortada = img.crop(region)
#imagen_recortada.show()
imagen_recortada.save(r'C:\Users\clauk\Desktop\Imagenes\0-copia recortada/'+a+'_3.tif')

region = (0,50,50,100)
imagen_recortada = img.crop(region)
#imagen_recortada.show()
imagen_recortada.save(r'C:\Users\clauk\Desktop\Imagenes\0-copia recortada/'+a+'_4.tif')

region = (50,50,100,100)
imagen_recortada = img.crop(region)
#imagen_recortada.show()
imagen_recortada.save(r'C:\Users\clauk\Desktop\Imagenes\0-copia recortada/'+a+'_5.tif')

region = (100,50,150,100)
imagen_recortada = img.crop(region)
#imagen_recortada.show()
imagen_recortada.save(r'C:\Users\clauk\Desktop\Imagenes\0-copia recortada/'+a+'_6.tif')

region = (0,100,50,150)
imagen_recortada = img.crop(region)
#imagen_recortada.show()
imagen_recortada.save(r'C:\Users\clauk\Desktop\Imagenes\0-copia recortada/'+a+'_7.tif')

region = (50,100,100,150)
imagen_recortada = img.crop(region)
#imagen_recortada.show()
imagen_recortada.save(r'C:\Users\clauk\Desktop\Imagenes\0-copia recortada/'+a+'_8.tif')

region = (100,100,150,150)
imagen_recortada = img.crop(region)
#imagen_recortada.show()
imagen_recortada.save(r'C:\Users\clauk\Desktop\Imagenes\0-copia recortada/'+a+'_9.tif')
