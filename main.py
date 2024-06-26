import flet as ft
from random import randint
from flet import Page, Row, Column, Image, Text, TextField, TextButton, FilledButton, NumbersOnlyInputFilter, KeyboardType, AlertDialog

def main(page: Page):
    page.theme = ft.Theme(color_scheme_seed=ft.colors.DEEP_PURPLE)
    page.title = "Randomizer"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.spacing = 25
    page.window.height = 400
    page.window.width = 500
    page.window.min_height = 350
    page.window.min_width = 400
    
    img = Image(src=f"icon.svg", width=50, height=50, fit=ft.ImageFit.CONTAIN)
    title = Text("Randomizer", theme_style=ft.TextThemeStyle.DISPLAY_SMALL)
    start_num = TextField(label="From", value="", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER, border_color=ft.colors.ON_BACKGROUND, focused_border_color=ft.colors.PRIMARY)
    end_num = TextField(label="To", value="", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER, border_color=ft.colors.ON_BACKGROUND, focused_border_color=ft.colors.PRIMARY)
    quantity = TextField(label="Quantity", value="", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER, border_color=ft.colors.ON_BACKGROUND, focused_border_color=ft.colors.PRIMARY)
    button_count = FilledButton(text="Count", disabled=True)
    cb_sort = ft.Checkbox(label="Sorting", value=True) 
    cb_repeat = ft.Checkbox(label="Repetitions", value=False)
    
    def randomizer(e):
        res_list = []
        while len(res_list) < int(quantity.value):
            n = randint(int(start_num.value), int(end_num.value))
            if not cb_repeat.value:
                if n not in res_list:
                    res_list.append(n)
            else:
                res_list.append(n)
        return res_list
    
    def sort_list(res_list):
        res_list = [int(i) for i in res_list]
        res_list = sorted(res_list)
        return res_list
    
    def list_to_str(res_list):
        res_str = ''
        sep = ', '
        
        for n in res_list:
            res_str += str(n)
            res_str += sep
    
        return res_str[:-2]
    
    def show_window(e, res_str):
        def close_win(e):
            popup_window.open = False
            page.update()
        
        def copy_result(e):
            page.set_clipboard(res_str)
        
        popup_window = AlertDialog(
            modal=True,
            title=Text("Result:"),
            content=ft.Container(
                content=Text(f'{res_str}', selectable=True), 
                padding=10,
                border_radius=10,
                border=ft.border.all(2, ft.colors.with_opacity(0.5, ft.colors.PRIMARY)),
                bgcolor=ft.colors.with_opacity(0.1, ft.colors.PRIMARY)
            ),
            actions=[
                TextButton("Copy", icon=ft.icons.COPY , on_click=copy_result),
                TextButton("Repeat", icon=ft.icons.REPEAT, on_click=print_result_in_window),
                TextButton("Close", icon=ft.icons.CLOSE, on_click=close_win),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )
        
        page.dialog = popup_window
        popup_window.open = True
        page.update()
    
    def print_result_in_window(e):
        res_list = randomizer(e)
        if cb_sort.value:
            res_list = sort_list(res_list)
        res_str = list_to_str(res_list)
        show_window(e, res_str)
    
    def validate(e):
        if all([start_num.value, end_num.value, quantity.value]):
            if cb_repeat.value or int(quantity.value) <= int(end_num.value):
                button_count.disabled = False
                quantity.error_text = None
                cb_repeat.is_error = False
            else:
                button_count.disabled = True
                quantity.error_text =  'Too big'
                cb_repeat.is_error = True
        else:
            button_count.disabled = True
            quantity.error_text =  None
            cb_repeat.is_error = False
        page.update()
    
    start_num.on_change = validate
    end_num.on_change = validate
    quantity.on_change = validate
    cb_repeat.on_change = validate
    button_count.on_click = print_result_in_window
    
    page.add(
        Row([img, title,], alignment="center"),
        Row([start_num, end_num, quantity], alignment="center"),
        Row([cb_sort, cb_repeat], alignment="center"),
        Row([button_count], alignment="center"))

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
