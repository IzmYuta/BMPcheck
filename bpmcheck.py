import sys


def main():
    arg = sys.argv
    header = get_file_header(arg)
    if is_it_BMP(header):
        data = get_BPM_data(header)
        print("{:<30} {:<20} {:<20} {:<20}".format("名前", "16進数", "16進数(LE)", "数値[単位]"))
        print("-" * 100)
        for key, value in data.items():
            print(
                "{:<20}\t {:<20}\t {:<20}\t {:<20}".format(
                    value["name"],
                    value["hex"],
                    value["hex_LE"],
                    str(value["int"]) + value["unit"],
                )
            )

    else:
        print("This file does not BMP.")


def get_file_header(arg):
    if len(arg) < 2:
        print("Input file name.", end="")
        filename = input()
    else:
        filename = arg[1]
    with open(f"{filename}", "rb") as f:
        header = f.read(54 * 2).hex()  # Read 54 bytes
    return header


def is_it_BMP(header):
    magic = header[0 : 2 * 2]
    if magic == "424d":
        return True
    else:
        return False


# Convert to Little Endian(LE)
def convert_to_LE(hex_BE):
    bytes_BE = bytes.fromhex(hex_BE)
    bytes_LE = bytes_BE[::-1]
    hex_LE = bytes_LE.hex()
    return hex_LE


def get_BPM_data(header):
    file_size = header[2 * 2 : 6 * 2]
    reserved_area1 = header[6 * 2 : 8 * 2]
    reserved_area2 = header[8 * 2 : 10 * 2]
    header_size = header[10 * 2 : 14 * 2]
    info_header_size = header[14 * 2 : 18 * 2]
    width = header[18 * 2 : 22 * 2]
    height = header[22 * 2 : 26 * 2]
    plain_num = header[26 * 2 : 28 * 2]
    colors_1px = header[28 * 2 : 30 * 2]
    compression_format = header[30 * 2 : 34 * 2]
    compression_size = header[34 * 2 : 38 * 2]
    horizontal_ppm = header[38 * 2 : 42 * 2]
    vertical_ppm = header[42 * 2 : 46 * 2]
    colors = header[46 * 2 : 50 * 2]
    important_colors = header[50 * 2 : 54 * 2]

    file_size_LE = convert_to_LE(file_size)
    reserved_area1_LE = convert_to_LE(reserved_area1)
    reserved_area2_LE = convert_to_LE(reserved_area2)
    header_size_LE = convert_to_LE(header_size)
    info_header_size_LE = convert_to_LE(info_header_size)
    width_LE = convert_to_LE(width)
    height_LE = convert_to_LE(height)
    plain_num_LE = convert_to_LE(plain_num)
    colors_1px_LE = convert_to_LE(colors_1px)
    compression_format_LE = convert_to_LE(compression_format)
    compression_size_LE = convert_to_LE(compression_size)
    horizontal_ppm_LE = convert_to_LE(horizontal_ppm)
    vertical_ppm_LE = convert_to_LE(vertical_ppm)
    colors_LE = convert_to_LE(colors)
    important_colors_LE = convert_to_LE(important_colors)

    data = {
        "file_size": {
            "name": "ファイルサイズ",
            "hex": file_size,
            "hex_LE": file_size_LE,
            "int": int(file_size_LE, 16),
            "unit": "バイト",
        },
        "reserved_area1": {
            "name": "予約領域1",
            "hex": reserved_area1,
            "hex_LE": reserved_area1_LE,
            "int": int(reserved_area1_LE, 16),
            "unit": "",
        },
        "reserved_area2": {
            "name": "予約領域2",
            "hex": reserved_area2,
            "hex_LE": reserved_area2_LE,
            "int": int(reserved_area2_LE, 16),
            "unit": "",
        },
        "header_size": {
            "name": "ヘッダサイズ",
            "hex": header_size,
            "hex_LE": header_size_LE,
            "int": int(header_size_LE, 16),
            "unit": "バイト",
        },
        "info_header_size": {
            "name": "情報ヘッダのサイズ",
            "hex": info_header_size,
            "hex_LE": info_header_size_LE,
            "int": int(info_header_size_LE, 16),
            "unit": "バイト",
        },
        "width": {
            "name": "画像の幅",
            "hex": width,
            "hex_LE": width_LE,
            "int": int(width_LE, 16),
            "unit": "px",
        },
        "height": {
            "name": "画像の高さ",
            "hex": height,
            "hex_LE": height_LE,
            "int": int(height_LE, 16),
            "unit": "px",
        },
        "plain_num": {
            "name": "プレーン数",
            "hex": plain_num,
            "hex_LE": plain_num_LE,
            "int": int(plain_num_LE, 16),
            "unit": "",
        },
        "colors_1px": {
            "name": "1画素の色数",
            "hex": colors_1px,
            "hex_LE": colors_1px_LE,
            "int": int(colors_1px_LE, 16),
            "unit": "",
        },
        "compression_format": {
            "name": "圧縮形式",
            "hex": compression_format,
            "hex_LE": compression_format_LE,
            "int": int(compression_format_LE, 16),
            "unit": "",
        },
        "compression_size": {
            "name": "圧縮サイズ",
            "hex": compression_size,
            "hex_LE": compression_size_LE,
            "int": int(compression_size_LE, 16),
            "unit": "バイト",
        },
        "horizontal_ppm": {
            "name": "水平解像度",
            "hex": horizontal_ppm,
            "hex_LE": horizontal_ppm_LE,
            "int": int(horizontal_ppm_LE, 16),
            "unit": "ppm",
        },
        "vertical_ppm": {
            "name": "垂直解像度",
            "hex": vertical_ppm,
            "hex_LE": vertical_ppm_LE,
            "int": int(vertical_ppm_LE, 16),
            "unit": "ppm",
        },
        "colors": {
            "name": "使用色数",
            "hex": colors,
            "hex_LE": colors_LE,
            "int": int(colors_LE, 16),
            "unit": "",
        },
        "important_colors": {
            "name": "重要色数",
            "hex": important_colors,
            "hex_LE": important_colors_LE,
            "int": int(important_colors_LE, 16),
            "unit": "",
        },
    }
    return data


if __name__ == "__main__":
    main()
