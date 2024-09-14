from psd_tools import PSDImage
import get_info, to_html, tools


def main():
    file_name = input("Please choose a file: ")
    tools.create_directories(file_name)
    psd_file = PSDImage.open(f'./raw/{file_name}.psd')
    print(f"    Image size：{psd_file.width} x {psd_file.height}")
    user_info = get_info.get_user_info()  # 包含用户输入的标题和原始psd图片尺寸
    user_info['width'] = psd_file.width
    user_info['height'] = psd_file.height
    layers_info = get_info.get_layers_info(file_name, psd_file, user_info)
    to_html.generate_html(file_name, layers_info, user_info)
    print('Done!')


if __name__ == "__main__":
    main()
