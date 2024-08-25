from FlasherPie.openOcd import OpenOcd

if __name__ == "__main__":
    openocd = OpenOcd()
    openocd.load_data("./test-data")
    source_dirs = openocd.source_dirs()
    if source_dirs:
        print(openocd.get_config(source_dirs[0]))
        openocd.flash(source_dirs[0])
