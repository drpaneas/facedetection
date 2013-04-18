    import SimpleCV
     
    cam = SimpleCV.Camera()
     
    while True:
        img = cam.getImage()
        faces = img.findHaarFeatures('haarcascade_frontalface_alt.xml')
        if faces:
            for face in faces:
                face.draw()
        img.show()
