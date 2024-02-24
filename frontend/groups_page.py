import flet as ft
from group_page import group
import requests
from pathlib import Path


def groups(page: ft.Page):
    page.title = 'Courses'

    def find_image(group_name: str):
        path = Path(__file__).parent / f"./pictures/{group_name}.png"
        return path

    def button_handler(_):
        print(_.__dict__)
        page.clean()
        page.client_storage.set("course_name", _.control.text)
        group(page)
        page.update()

    def groups_setup() -> ft.Column:
        courses_request = requests.get(
            url="http://127.0.0.1:4000/api/users/courses",
            headers={"authorization": f"{page.client_storage.get('token')}"}
        )
        reqs = courses_request.json()
        groups_title = ft.Text(
            value="My courses",
            size=36
        )
        groups_grid = ft.GridView(
            expand=100,
            runs_count=20,
            max_extent=400,
            child_aspect_ratio=1.0,
            spacing=10,
            run_spacing=10,
        )
        for course in reqs["courses"]:
            try:
                path = find_image(course["_id"])
            except FileNotFoundError:
                path = ""
            course_card = ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Image(
                                        src=path,
                                    ),
                                ],
                                width=250,
                                height=80,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.ListTile(
                                title=ft.Text(f"Introductory computer science 1"),
                                subtitle=ft.Text(
                                    f"{course["name"]["description"]}"
                                ),
                            ),
                            ft.ElevatedButton(
                                f"{course["name"]["shortName"]}",
                                on_click=button_handler
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=400,
                    padding=10,

                )
            )
            groups_grid.controls.append(course_card)
        page.client_storage.set("courses_loaded", "true")
        form_container = ft.Column(
            height=850,
            width=1650,
            spacing=80,
            controls=[groups_title, groups_grid, ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        return form_container

    page.add(ft.Row(
        [
            groups_setup(),
        ],
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    ))
