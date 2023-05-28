from dozing_off.models import camera

def management():
    print(f'======================================')
    print(f'I am a Camera Manager! Doze detection.')
    print(f'======================================')
    camera = camera.Camera()
    # camera.find_the_camera()
    camera.dozing_off()
