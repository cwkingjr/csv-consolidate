from nicegui import app, ui
from webview import FOLDER_DIALOG

app.native.window_args["resizable"] = False
# app.native.start_args["debug"] = True
app.native.settings["ALLOW_DOWNLOADS"] = True


@ui.page("/")
def main_page():
    async def pick_directory():
        folder = await app.native.main_window.create_file_dialog(
            allow_multiple=False,
            dialog_type=FOLDER_DIALOG,
        )
        if folder:
            ui.notify(f"Selected directory: {folder}")
        else:
            ui.notify("No directory selected.")

    ui.label("app running in native mode")
    ui.button("enlarge", on_click=lambda: app.native.main_window.resize(1000, 700))
    ui.button("Pick Directory", on_click=pick_directory)


ui.run(
    title="CSV Consolidate",
    native=True,
    window_size=(400, 300),
    fullscreen=False,
    reload=False,
)
