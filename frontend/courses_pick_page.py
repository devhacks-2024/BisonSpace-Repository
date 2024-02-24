import flet as ft
import requests
from content_page import content
from pathlib import Path


def courses_pick(page: ft.Page) -> any:
    page.title = "Course pick"
    page.padding = 50
    page.scroll = ft.ScrollMode.ADAPTIVE
    choosen_courses = []

    def find_image(group_name: str):
        path = Path(__file__).parent / f"./pictures/{group_name}.png"
        return path

    def continue_handler(_):
        data = {
            "courses": choosen_courses
        }
        continue_request = requests.post(
            "http://127.0.0.1:4000/api/users/addCourses",
            json=data,
            headers={"authorization": f"{page.client_storage.get('token')}"}
        )
        if continue_request.status_code == 200:
            page.clean()
            content(page)
            page.update()

    def checkbox_handler(_):
        if _.data == "true":
            choosen_courses.append(_.control.label)
        elif _.data == "false":
            choosen_courses.remove(_.control.label)

    def grid_setup() -> ft.Column:
        courses_requests = requests.get("http://127.0.0.1:4000/api/courses")
        courses_json = courses_requests.json()

        title = ft.Text(
            value="Choose your current term courses",
            size=36,
            height=100
        )
        continue_button = ft.ElevatedButton(
            width=110,
            height=40,
            text="Continue",
            style=ft.ButtonStyle(
                bgcolor=ft.colors.BLACK45,
            ),
            on_click=continue_handler
        )
        courses_grid = ft.GridView(
            expand=150,
            runs_count=5,
            max_extent=400,
            child_aspect_ratio=0.9,
            spacing=10,
            run_spacing=10,
        )

        for course in courses_json["courses"]:
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
                                title=ft.Text(f"{course["name"]["officialName"]}"),
                                subtitle=ft.Text(
                                    f"{course["name"]["description"][0:80]}..."
                                ),
                            ),
                            ft.CupertinoCheckbox(
                                label=f"{course["_id"]}",
                                on_change=checkbox_handler
                            )
                        ],
                    ),
                    width=400,
                    padding=10,
                )
            )
            courses_grid.controls.append(course_card)
        form_container = ft.Column(
            height=850,
            width=900,
            spacing=80,
            controls=[title, courses_grid, continue_button],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        return form_container

    page.add(ft.Row(
        [
            grid_setup(),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    ))
