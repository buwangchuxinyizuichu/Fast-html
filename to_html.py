def generate_html(layers_info, user_info):
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name=”viewport” content="width=device-width, initial-scale=1.0">
        <style>
            * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body,
        html {{
            margin: 0;
            padding: 0;
            background-color: white;
            overflow: auto;
            width: 100%;
            height: 100%;
        }}

        .container {{
            display: flex;
            flex-direction: column;
            width: 100%;
            height: 0;
            padding-bottom: {user_info['height']/user_info['width']*100}%;
            position: relative;
        }}

        .layer {{
            position: absolute;
            width: 100%;
            height: auto;
            max-width: 100%;
        }}

        .text-layer {{
            font-family: Arial, sans-serif;
            white-space: pre-wrap;
        }}
        @media (max-width: 768px) {{
            .container {{
                height: auto;
                padding-bottom: 0;
                overflow-y: auto;
            }}
            .content {{
                position: relative;
            }}
            .layer {{
                position: relative;
                margin-bottom: 10px;
            }}
            .text-layer {{
                font-size: 14px !important;
                width: 90% !important;
                left: 5% !important;
                margin: 10px 0;
            }}
            .text-layer p {{
                font-size: clamp(12px, 5vw, 24px);
                line-height: 1.2;
                margin: 0;
                position: absolute;
                transform: translateY(-50%);
            }}
        }}
    </style>
        <title>{user_info['title']}</title>
    </head>
    <body>
        <div class="container">
    '''
    for layer_info in layers_info:
        if not layer_info['visible']:
            continue
        style = f"left: {layer_info['left']/user_info['width']*100}%; top: {layer_info['top']/user_info['height']*100}%; width: {layer_info['width']/user_info['width']*100}%; height: {layer_info['height']/user_info['height']*100}%; opacity: {layer_info['opacity']/255};"
        if layer_info['type'] == 'text':
            color = f"rgba({int(layer_info['color'][1] * 255)}, {int(layer_info['color'][2] * 255)}, {int(layer_info['color'][3] * 255)}, {layer_info['color'][0]})"
            html_content += f'''
                <div class="layer text-layer" style="{style} font-family: {layer_info['font']}; font-size: auto; color: {color};">
                    <p> {layer_info['text']}    </p>
                </div>
        '''
        elif layer_info['type'] == 'image':
            html_content += f'''
                <img src="{layer_info['image_path']}" class="layer" style="{style}">
        '''

    html_content += '''
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
            <script src="jquery.fittext.js"></script>
            <script>
                $(document).ready(function () {
                    $(".text-layer p").fitText();
                });
            </script>
        </div>
    </body>
    </html>
    '''
    with open("./results/output.html", 'w', encoding='utf-8') as f:
        f.write(html_content)