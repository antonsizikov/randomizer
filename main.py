import flet
from random import randint
from flet import Page, Row, Column, Text, TextThemeStyle, TextField, NumbersOnlyInputFilter, KeyboardType, OutlinedButton, Container, AlertDialog, TextButton

def main(page: Page):
    page.title = "Randomizer"
    page.vertical_alignment = "center"
    page.window_height = 400
    page.window_width = 500
    
    start_num = TextField(label="From", value="", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    end_num = TextField(label="To", value="", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    quantity = TextField(label="Quantity", value="", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    button_copy = OutlinedButton(text="Copy")
    button_count = OutlinedButton(text="Count", disabled=True)
    
    def randomizer(e):
        i = 1
        res_list = []
        while i <= int(quantity.value):
            res_list.append(str(randint(int(start_num.value), int(end_num.value))))
            i = i + 1
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
        res_list = sort_list(res_list)
        res_str = list_to_str(res_list)
        show_window(e, res_str)
    
    def validate(e):
        if all([start_num.value, end_num.value, quantity.value]):
            button_count.disabled = False
        else:
            button_count.disabled = True
        page.update()
    
    def copy_result(e, res_str):
        page.set_clipboard(res_str)
    
    start_num.on_change = validate
    end_num.on_change = validate
    quantity.on_change = validate
    button_count.on_click = print_result_in_window
    button_copy.on_click = copy_result
    
    page.add(
        Row(
            [
            Text("Randomizer", theme_style=TextThemeStyle.DISPLAY_SMALL),
            ],
            alignment="center",
        ),

        Row(
            [
                Column(
                    [
                        start_num,
                    ],
                    alignment="center",
                ),
                Column(
                    [
                        end_num,
                    ],
                    alignment="center",
                ),
                Column(
                    [
                        quantity,
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
        ),
        Row(
            [
                button_count,
            ],
            alignment="center",
        ),
    )


if __name__ == "__main__":
    flet.app(target=main)
