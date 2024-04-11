import flet
from random import randint
from flet import IconButton, Page, Row, Column, TextField, icons, Text, TextThemeStyle, ElevatedButton, NumbersOnlyInputFilter, KeyboardType

def main(page: Page):
    page.title = "Randomizer"
    page.vertical_alignment = "center"
    page.window_height = 400
    page.window_width = 500
    
    start_num = TextField(label="From", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    end_num = TextField(label="To", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    quantity = TextField(label="Count", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)

    def randomizer(e):
        i = 1
        result = []
        while i <= int(quantity.value):
            result.append(str(randint(int(start_num.value), int(end_num.value))))
            i = i + 1
        print(result)
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
                ElevatedButton(text="Submit", on_click=randomizer),
            ],
            alignment="center",
        ),
    )

flet.app(target=main)
