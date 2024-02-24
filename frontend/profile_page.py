import flet as ft
from avatar_generator import generator


def profile(page: ft.Page):
    page.title = "Content"
    first_column = ft.Column(
        width=500,
        height=800,
    )
    first_column.controls.append(
        generator(
            first_name=page.client_storage.get("user_first_name"),
            last_name=page.client_storage.get("user_last_name"),
            default_color=page.client_storage.get("user_default_color"),
            picture_width=300,
            picture_height=300,
            text_size=100
        )
    )
    second_column = ft.Column(
        width=800,
        height=800,
    )
    second_column.controls.append(
        ft.Column(
            [ft.Text(
                f"First name: {page.client_storage.get("user_first_name")}",
                size=24
            ),
                ft.Text(
                    f"Last name: {page.client_storage.get("user_last_name")}",
                    size=24
                ),
            ],

        ),
    )
    page.add(ft.Row(
        [first_column, second_column]
    ))
