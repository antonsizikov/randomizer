import flet
from random import randint
from flet import Page, Row, Column, Text, TextThemeStyle, TextField, NumbersOnlyInputFilter, KeyboardType, OutlinedButton, Container, AlertDialog, TextButton, colors

def main(page: Page):
    page.title = "Randomizer"
    page.vertical_alignment = "center"
    page.window_height = 400
    page.window_width = 500
    
    start_num = TextField(label="From", value="1", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    end_num = TextField(label="To", value="10", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    quantity = TextField(label="Count", value="1", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    button_count = OutlinedButton(text="Count")
    button_copy = OutlinedButton(text="Copy")
        
    def randomizer(e):
        i = 1
        res_list = []
        while i <= int(quantity.value):
            res_list.append(str(randint(int(start_num.value), int(end_num.value))))
            i = i + 1
        #print(result)        
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
    
    def print_result(res_str):
        page.add(
            Row(
                [
                    Container(
                        content=Text(f'{res_str}'),
                        margin=0,
                        padding=10,
                        bgcolor=flet.colors.GREY_500,
                        border_radius=10,
                        ink=True,
                        on_click=copy_result
                        ),
                ],
            alignment="center",
            )
        )
    
    def main_rand(e):
        res_list = randomizer(e)
        res_list = sort_list(res_list)
        res_str = list_to_str(res_list)
        print_result(res_str)
    
    def validate(e):
        if all([start_num.value, end_num.value, quantity.value]):
            button_count.disabled = False
        else:
            button_count.disabled = True
        page.update()
    
    def copy_result(e):
        page.set_clipboard("This value comes from Flet app")
    
    start_num.on_change = validate
    end_num.on_change = validate
    quantity.on_change = validate
    button_count.on_click = main_rand
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
                button_copy,
            ],
            alignment="center",
        ),
        Row(
            [
                Text(f"Results:", theme_style=TextThemeStyle.BODY_LARGE),
            ],
            alignment="center",
        ),
    )


if __name__ == "__main__":
    flet.app(target=main)
