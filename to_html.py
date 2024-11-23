from tqdm import tqdm


def generate_style(layer_info, user_info):
    style_content = f'''
        .{layer_info['name']}{{
            position: absolute;
            left: {layer_info['left']/16}rem;
            top: {layer_info['top']/16}rem;
            width: {layer_info['width']/16}rem;
            height: {layer_info['height']/16}rem;
            opacity: {layer_info['opacity']/255};
            line-height: {layer_info['line_height']/16}rem;
        }}\n
    '''
    return style_content


def generate_html(file_name, layers_info, user_info):
    html_content = f'''
    <!DOCTYPE html5>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name=”viewport” content="width=device-width, initial-scale=1.0">
        <title>{user_info['title']}</title>
        <link rel="stylesheet" href="static/css/styles.css" />
        <style>
            body,
            html {{
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                scroll-behavior: smooth;
            }}
        </style>

    '''
    style_content = '<style>\n'
    body_content = f'''
    <body>
    '''
    for layer_info in tqdm(layers_info):
        if not layer_info['visible']:
            continue
        style_content += generate_style(layer_info, user_info)
        if layer_info['type'] == 'text':
            color = f"rgba({int(layer_info['color'][1] * 255)}, {int(layer_info['color'][2] * 255)}, {int(layer_info['color'][3] * 255)}, {layer_info['color'][0]})"
            body_content += f'''
                <div class="{layer_info['name']}" style="font-family: {layer_info['font']}; font-size: {layer_info['font_size']}; color: {color};">
                    <p> {layer_info['text']}    </p>
                </div>
        '''
        elif layer_info['type'] == 'image':
            body_content += f'''
            <div class="{layer_info['name']}">
                <img src="{layer_info['image_path']}">
            </div>
        '''
    style_content += '</style>\n'
    with open(f"./results/{file_name}/static/css/styles.css", 'w', encoding='utf-8') as f:
        f.write(style_content)
    html_content += '</head>\n' + body_content
    html_content += '''
        <script>
            var browserWidth = window.innerWidth;
            var browserHeight = window.innerHeight;
        </script>
    '''
    html_content += '''
    </body>
    </html>
    '''
    with open(f"./results/{file_name}/output.html", 'w', encoding='utf-8') as f:
        f.write(html_content)
