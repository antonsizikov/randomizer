import flet
from random import randint
from flet import IconButton, Page, Row, Column, TextField, icons, Text, TextThemeStyle, ElevatedButton

def main(page: Page):
    page.title = "Randomizer"
    page.vertical_alignment = "center"
    page.window_height = 400
    page.window_width = 500
    
    start_num = TextField(label="From", text_align="right", width=100)
    end_num = TextField(label="To", text_align="right", width=100)
    quantity = TextField(label="Count", text_align="right", width=100)
    
    def pass_func():
        pass
    
    def print_result(a):
        print(a)
    
    def randomizer(start_num, end_num, quantity):
        i = 1
        result = ''
        while i <= int(quantity.value):
            #print(str(randint(int(start_num.value), int(end_num.value))))
            result += str(randint(int(start_num.value), int(end_num.value)))
            i = i + 1
        return result
    
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
                ElevatedButton(text="Submit", on_click=pass_func),
            ],
            alignment="center",
        ),
    )

flet.app(target=main)
