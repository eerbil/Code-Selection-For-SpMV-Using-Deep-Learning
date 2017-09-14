import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

size = 400, 400
matrices = os.listdir("images")
print len(matrices)
for infile in matrices:
    print infile
    try:
        im = Image.open("/home/eliferbil/Code-Selection-For-SpMV-Using-Deep-Learning/images/"+ infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save("/home/eliferbil/Code-Selection-For-SpMV-Using-Deep-Learning/image_400/" + infile, "png")
    except IOError:
        print "cannot create thumbnail for '%s'" % infile
