from psd_tools import PSDImage
import get_info, to_html, tools


def init_html(file_name, title):
    tools.create_directories(file_name)
    psd_file = PSDImage.open(f'./raw/{file_name}.psd')
    print(f"    Image size：{psd_file.width} x {psd_file.height}")
    user_info = {'title': title, 'width': psd_file.width, 'height': psd_file.height}
    layers_info = get_info.get_layers_info(file_name, psd_file, user_info)
    to_html.generate_html(file_name, layers_info, user_info)
    print('Done!')

