import flet as ft

from content_page import content


def courses_pick(page: ft.Page) -> any:
    page.title = "Course pick"
    page.padding = 50
    page.scroll = ft.ScrollMode.ADAPTIVE
    choosen_courses = []
    courses_list = ["comp 1010", "comp 1020", "comp 2020", "comp 1010", "comp 1020", "comp 2020", "comp 1010",
                    "comp 1020", "comp 2020", "comp 1010", "comp 1020", "comp 1010", "comp 1020", "comp 1010",
                    "comp 1020", "comp 2020", "comp 1010", "comp 1020", "comp 2020", "comp 1010",
                    "comp 1020", "comp 2020", "comp 1010", "comp 1020", "comp 1010", "comp 1020", ]

    def courses_handler(_):
        page.clean()
        content(page)

    def checkbox_handler(_):
        if _.data == "true":
            choosen_courses.append(_.control.label)
        elif _.data == "false":
            choosen_courses.remove(_.control.label)

    def grid_setup() -> ft.Column:
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
            on_click=courses_handler
        )
        courses_grid = ft.GridView(
            expand=50,
            runs_count=20,
            max_extent=250,
            child_aspect_ratio=1.0,
            spacing=10,
            run_spacing=50,
        )
        for course in courses_list:  # change to course from db
            course_card = ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.ALBUM),
                                title=ft.Text("Introductory computer science 1"),
                                subtitle=ft.Text(
                                    "Programming coursrogramming course..rogramming course..rogramming course..e.."
                                ),
                            ),
                            ft.CupertinoCheckbox(
                                label=f"{course}",
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
