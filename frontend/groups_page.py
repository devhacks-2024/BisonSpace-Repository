import flet as ft


def groups(page: ft.Page):
    page.title = "Courses"
    courses_list = ["comp 1010", "comp 1020", "comp 2020"]

    def button_handler(_):
        print("here")

    def groups_setup() -> ft.Column:
        groups_grid = ft.GridView(
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
                                title=ft.Text(f"Introductory computer science 1 - [{course}]"),
                                subtitle=ft.Text(
                                    "Programming coursrogramming course..rogramming course..rogramming course..e.."
                                ),
                            ),
                            ft.ElevatedButton(
                                f"Go into",
                                on_click=button_handler
                            )
                        ],
                    ),
                    width=400,
                    padding=10,
                )
            )
            groups_grid.controls.append(course_card)
        form_container = ft.Column(
            height=850,
            width=900,
            spacing=80,
            controls=[groups_grid, ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        return form_container

    page.add(ft.Row(
        [
            groups_setup(),
        ],
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    ))
