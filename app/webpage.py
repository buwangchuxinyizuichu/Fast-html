from nicegui import ui
import main
import tools
import functions

def run_webgui():

    def check(selected_file):
        if not selected_file.value:
            selected_file.style('border: 1px solid red;')
        elif not title.value:
            selected_file.style('border: 1px solid white;')
            title.style('border: 1px solid red;')
        else:
            title.style('border: 1px solid white;')
            functions.init_html(selected_file.value[:-4], title.value)

    with ui.card().style('width: 40%;'):
        selected_file = ui.select(label='Select a file', options=tools.get_raw_files()).style('width: 100%; overflow:hidden;')
        title = ui.input(label='Title').style(' width: 100%;')
        with ui.row():
            ui.button('Initialize', on_click=lambda: check(selected_file))

    ui.run()
