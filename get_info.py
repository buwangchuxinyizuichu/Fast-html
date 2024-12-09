from PIL import Image


def get_layer(file_name, layer, layers_info, user_info):
    if layer.is_group():
        if layer.visible:
            for sub_layer in layer._layers:
                get_layer(file_name, sub_layer, layers_info, user_info)
    else:
        replacements = [
            ' ',
            '.',
            '?',
            '!',
            '@',
            '#',
            '$',
            "%",
            "^",
            "&",
            "*",
            "-",
            "+",
            "=",
            ":",
            ";",
            ",",
            "<",
            ">",
            "/",
            "\\",
            "|",
            "{",
            "}",
            "[",
            "]",
            "(",
            ")",
            "'",
            '"',
            "`",
            "~",
            "，",
            "、",
            "。",
            "；",
            "：",
            "？",
            "！",
            "“",
            "”",
            "‘",
            "’",
            "（",
            "）",
            "【",
            "】",
            "《",
            "》",
            "——",
        ]
        for replacement in replacements:
            layer.name = layer.name.replace(replacement, '-')
        layer_info = {
            'name': f"块_{layer.name}_{layer.left}_{layer.top}_{layer.width}_{layer.height}",
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
            try:
                layer_info['font'] = layer._engine_data['ResourceDict']['FontSet'][0]['Name']
            except:
                layer_info['font'] = 'default-font'
                print('Warning: font not found !')
            layer_info['font_size'] = layer.engine_dict['StyleRun']['RunArray'][0]['StyleSheet']['StyleSheetData'].get('FontSize', 12)
            layer_info['color'] = layer.engine_dict['StyleRun']['RunArray'][0]['StyleSheet']['StyleSheetData'].get('FillColor', {'Values': [1, 0, 0, 0]}).get('Values', [1, 0, 0, 0])
            layer_info['line_height'] = layer.engine_dict['StyleRun']['RunArray'][0]['StyleSheet']['StyleSheetData'].get('Leading', 12)
            layer_info['top'] -= 24
            layer_info['width'] += 16
        else:
            layer_image = layer.composite()
            if layer_image:
                pil_image = Image.frombytes('RGBA', layer_image.size, layer_image.tobytes())
                try:
                    pil_image.save(f"./results/{file_name}/static/img/{layer_info['name']}.png")
                    layer_info['image_path'] = f"./static/img/{layer_info['name']}.png"
                except:
                    return
            layer_info['line_height'] = 0
        layers_info.append(layer_info)


def get_layers_info(file_name, psd_file, user_info):
    layers_info = []
    for index, root_layer in enumerate(psd_file._layers):
        get_layer(file_name, root_layer, layers_info, user_info)
    return layers_info
