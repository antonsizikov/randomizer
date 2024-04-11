import flet
from random import randint
from flet import Page, Row, Column, Text, TextThemeStyle, TextField, NumbersOnlyInputFilter, KeyboardType, OutlinedButton

def main(page: Page):
    page.title = "Randomizer"
    page.vertical_alignment = "center"
    page.window_height = 400
    page.window_width = 500
    
    start_num = TextField(label="From", value="1", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    end_num = TextField(label="To", value="10", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)
    quantity = TextField(label="Count", value="1", text_align="right", width=100, input_filter=NumbersOnlyInputFilter(), keyboard_type=KeyboardType.NUMBER)

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
                OutlinedButton(text="Count", on_click=randomizer),
            ],
            alignment="center",
        ),
        Row(
            [
                Text(f"Results:\n", theme_style=TextThemeStyle.BODY_LARGE),
            ],
            alignment="center",
        ),
    )

flet.app(target=main)
