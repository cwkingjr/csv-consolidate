from nicegui import app, ui


app.native.window_args["resizable"] = False
# app.native.start_args["debug"] = True
app.native.settings["ALLOW_DOWNLOADS"] = True


@ui.page("/")
def main_page():
    ui.label("app running in native mode")
    ui.button("enlarge", on_click=lambda: app.native.main_window.resize(1000, 700))


ui.run(title="CSV Consolidate", native=True, window_size=(400, 300), fullscreen=False)
