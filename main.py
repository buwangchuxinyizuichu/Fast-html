from psd_tools import PSDImage
import get_info, to_html

def main():
    psd_file = PSDImage.open(f'./raw/{input("Please choose a file: ")}.psd')
    print(f"    Image size：{psd_file.width} x {psd_file.height}")
    user_info = get_info.get_user_info()
    user_info['width'] = psd_file.width
    user_info['height'] = psd_file.height
    layers_info = get_info.get_layers_info(psd_file, user_info)
    to_html.generate_html(layers_info, user_info)


if __name__ == "__main__":
    main()