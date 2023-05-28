import dozing_off.controller.camera_manager

def main():
    # Start of doze detection
    print(f'Start of doze detection')
    dozing_off.controller.camera_manager.management()
    # End of doze detection
    print(f'End of doze detection')

if __name__ == '__main__':
    main()
