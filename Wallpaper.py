import platform
import logging


class Wallpaper:
    def change(self, image_path):
        """
        Changes the desktop wallpaper to the image whose path is provided. This function
        checks if the given path is a valid one, then executed platform dependent code to
        change the wallpaper.

        :param image_path: The path to the desired wallpaper.
        :raises IOError If the path provided is invalid (not a file)
        :raises Exception If the current platform is not supported.
        """
        # Check if the given path is a valid one
        import os.path
        if not os.path.isfile(image_path):
            logging.error("The path provided is invalid (not a file) : {}" % image_path)
            raise IOError("Invalid file name.")

        # Get the operating system
        operating_system = platform.system().lower()
        logging.info("The Operating System detected is " + operating_system)

        if operating_system == "windows":
            # We need to make use of DLLs in this case
            self.change_wallpaper_on_windows(image_path)
        elif operating_system == "linux":
            # A simple command will work
            import os
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + image_path)
        else:
            raise Exception("Platform not supported currently.")

    # This is the attribute used when setting the wallpaper on Windows
    SPI_SETDESKWALLPAPER = 20

    def change_wallpaper_on_windows(self, image_path):
        """
        Changes the wallpaper on windows. Assumes that the path given has
        been checked for validity.

        :param image_path: The validated path to the image.
        """
        import ctypes
        if platform.architecture()[0] == "64bit":
            ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER, 0, image_path, 0)
        else:
            ctypes.windll.user32.SystemParametersInfoA(self.SPI_SETDESKWALLPAPER, 0, image_path, 0)
