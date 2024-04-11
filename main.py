import flet
from flet import IconButton, Page, Row, Column, TextField, icons, Text, TextThemeStyle

def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"
    page.window_height = 400
    page.window_width = 500
    
    start_num = TextField(label="From", text_align="right", width=100)
    end_num = TextField(label="To", text_align="right", width=100)
    quantity = TextField(label="Count", text_align="right", width=100)
    
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
    )

flet.app(target=main)
