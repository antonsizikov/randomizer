import flet as ft
from random import randint
from flet import Page, Row, Column, Image, Text, TextField, TextButton, FilledButton, NumbersOnlyInputFilter, KeyboardType, AlertDialog

def main(page: Page):
    page.theme = ft.Theme(color_scheme_seed=ft.colors.DEEP_PURPLE)
    page.title = "Randomizer"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_height = 400
    page.window_width = 500
    
    img = Image(src=f"/Volumes/Files/Code/Python/flet/Randomizer/assets/icon.svg", width=50, height=50, fit=ft.ImageFit.CONTAIN)
    title = Text("Randomizer", theme_style=ft.TextThemeStyle.DISPLAY_SMALL)
    start_num = TextField(label="From", value="", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    end_num = TextField(label="To", value="", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    quantity = TextField(label="Quantity", value="", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
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
        
        popup_window = AlertDialog(
            modal=True,
            title=Text("Result:"),
            content=Text(f'{res_str}'),
            actions=[
                TextButton("Copy", on_click=copy_result(e, res_str)),
                TextButton("Close", on_click=close_win),
            ],
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
            else:
                button_count.disabled = True
        else:
            button_count.disabled = True
        page.update()
    
    def copy_result(e, res_str):
        page.set_clipboard(res_str)
    
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
    ft.app(target=main)
