from PIL import Image


def check_width(layer_info, user_info):
    if layer_info['left'] + layer_info['width'] > user_info['width']:
        return True


def check_height(layer_info, user_info):
    if layer_info['top'] + layer_info['height'] > user_info['height']:
        return True


def get_layer(file_name, layer, layers_info, user_info):
    if layer.is_group():
        for sub_layer in layer._layers:
            get_layer(file_name, sub_layer, layers_info, user_info)
    else:
        layer_info = {
            'name': f"{layer.name.replace(' ', '-')}_{layer.left}_{layer.top}_{layer.width}_{layer.height}",
            'type': 'text' if layer.kind == 'type' else 'image',
            'left': layer.left,
            'top': layer.top,
            'width': layer.width,
            'height': layer.height,
            'opacity': layer.opacity,
            'visible': layer.visible
        }
        if layer_info['left'] > user_info['width'] or layer_info['top'] > user_info['height'] or layer_info['left'] + layer_info['width'] < 0 or layer_info['top'] + layer_info['height'] < 0:
            return
        if layer.kind == 'type':
            layer_info['text'] = layer.text
            run_array = layer.engine_dict.get('StyleRun', {}).get('RunArray', [{}])
            style_sheet = run_array[0].get('StyleSheet', {})
            layer_info['font'] = style_sheet.get('FontPostScriptName', 'default-font')
            layer_info['font_size'] = layer.engine_dict['StyleRun']['RunArray'][0]['StyleSheet']['StyleSheetData'].get('FontSize', 12)
            layer_info['color'] = layer.engine_dict['StyleRun']['RunArray'][0]['StyleSheet']['StyleSheetData'].get('FillColor', {'Values': [0, 0, 0, 1]}).get('Values', [0, 0, 0, 1])
            '''
            if layer_info['left'] < 0 or (layer, user_info) or check_height(layer, user_info):
                print(f'Warning: The text "{layer.text}" may exceed the page !')
            '''
        else:
            layer_image = layer.composite()
            if layer_image:
                pil_image = Image.frombytes('RGBA', layer_image.size, layer_image.tobytes())
                if layer_info['left'] < 0:
                    pil_image = pil_image.crop((-layer_info['left'], 0, layer_info['width'], layer_info['height']))
                    layer_info['width'] += layer_info['left']
                    layer_info['left'] = 0
                if check_width(layer_info, user_info):
                    pil_image = pil_image.crop((0, 0, user_info['width'] - layer_info['left'], layer_info['height']))
                    layer_info['width'] -= layer_info['left'] + layer_info['width'] - user_info['width']
                if layer_info['top'] < 0:
                    pil_image = pil_image.crop((0, -layer_info['top'], layer_info['width'], layer_info['height']))
                    layer_info['height'] += layer_info['top']
                    layer_info['top'] = 0
                if check_height(layer_info, user_info):
                    pil_image = pil_image.crop((0, 0, layer_info['width'], user_info['height'] - layer_info['top']))
                    layer_info['width'] -= layer_info['top'] + layer_info['height'] - user_info['height']
                try:
                    pil_image.save(f"./results/{file_name}/assets/images/{layer_info['name']}.png")
                    layer_info['image_path'] = f"./assets/images/{layer_info['name']}.png"
                except:
                    return
        layers_info.append(layer_info)


def get_layers_info(file_name, psd_file, user_info):
    layers_info = []
    for index, root_layer in enumerate(psd_file._layers):
        get_layer(file_name, root_layer, layers_info, user_info)
    return layers_info
