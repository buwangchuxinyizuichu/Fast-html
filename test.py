from nicegui import ui


def on_button_click():
    file_name = ui.text.value
    # 在这里添加你的代码


ui.text('Please choose a file: ', on_enter=on_button_click)
ui.button('Submit', on_click=on_button_click)

ui.run()
