import psutil


def get_memory_card_paths():
    memory_card_paths = []
    valid_fstypes = ["vfat", "exfat", "msdos"]

    partitions = psutil.disk_partitions()
    for partition in partitions:
        opts = partition.opts.split(",")
        if (partition.fstype.lower() in valid_fstypes) or (
            ("local" in opts)
            and ("rw" in opts)
            and ("nosuid" in opts)
            and ("noexec" not in opts)
        ):
            memory_card_paths.append(partition.mountpoint)

    return memory_card_paths
