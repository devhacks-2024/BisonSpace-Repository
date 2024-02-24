import flet as ft


def generator(first_name: str, last_name: str, default_color: str) -> ft.Container:
    letters = first_name[0].upper() + last_name[0].upper()
    avatar = ft.Container(
        content=ft.Text(f"{letters}"),
        width=100,
        height=100,
        border_radius=50,
        bgcolor=default_color
    )
    return avatar
