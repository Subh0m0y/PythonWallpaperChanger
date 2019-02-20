import Wallpaper


def main():
    folder = "sample_images"
    image_name = "chuttersnap-510131-unsplash.jpg"
    import os
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder, image_name)

    wallpaper = Wallpaper.Wallpaper()
    wallpaper.change(image_path)


if __name__ == '__main__':
    main()
