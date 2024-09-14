from tqdm import tqdm


def generate_style(layer_info, user_info, num):
    style_content = f'''
        .n{num}{{
            position: absolute;
            left: {layer_info['left']/user_info['width']*100}%;
            top: {layer_info['top']}px;
            width: {layer_info['width']/user_info['width']*100}%;
            height: auto;
            opacity: {layer_info['opacity']/255};
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
        <style>
            body,
            html {{
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                scroll-behavior: smooth;
            }}

    '''
    style_content = ''
    body_content = f'''
    <body>
    '''
    num = 1  # 图层计数器
    for layer_info in tqdm(layers_info):
        if not layer_info['visible']:
            continue
        style_content += generate_style(layer_info, user_info, num)
        if layer_info['type'] == 'text':
            color = f"rgba({int(layer_info['color'][1] * 255)}, {int(layer_info['color'][2] * 255)}, {int(layer_info['color'][3] * 255)}, {layer_info['color'][0]})"
            body_content += f'''
                <div class="n{num}" font-family: {layer_info['font']}; font-size: auto; color: {color};>
                    <p> {layer_info['text']}    </p>
                </div>
        '''
        elif layer_info['type'] == 'image':
            body_content += f'''
            <div class="n{num}">
                <img src="{layer_info['image_path']}">
            </div>
        '''
        num += 1

    html_content += style_content + '\n</style>\n</head>\n' + body_content
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
