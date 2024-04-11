import flet
from flet import IconButton, Page, Row, Column, TextField, icons, Text, TextThemeStyle

def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"
    page.window_height = 400
    page.window_width = 500
    
    num_from = TextField(value="", text_align="right", width=100)
    num_to = TextField(value="", text_align="right", width=100)
    num_count = TextField(value="", text_align="right", width=100)
    
    page.add(
        Row(
            [
            Text("Randimizer", theme_style=TextThemeStyle.DISPLAY_SMALL),
            ],
            alignment="center",
        ),

        Row(
            [
                Column(
                    [
                        Text("From", theme_style=TextThemeStyle.TITLE_MEDIUM),
                        num_from,
                    ],
                    alignment="center",
                ),
                Column(
                    [
                        Text("To", theme_style=TextThemeStyle.TITLE_MEDIUM),
                        num_to,
                    ],
                    alignment="center",
                ),
                Column(
                    [
                        Text("Count", theme_style=TextThemeStyle.TITLE_MEDIUM),
                        num_count,
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
        ),
    )

flet.app(target=main)
