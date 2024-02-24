import flet as ft


def generator(
        first_name: str,
        last_name: str,
        default_color: str,
        text_size: int,
        picture_width: int,
        picture_height: int
) -> ft.Container:
    letters = first_name[0].upper() + last_name[0].upper()
    avatar = ft.Container(
        content=ft.Text(
            f"{letters}",
            size=text_size
        ),
        width=picture_width,
        height=picture_height,
        border_radius=50,
        bgcolor=default_color,
        alignment=ft.alignment.center,
    )
    return avatar
