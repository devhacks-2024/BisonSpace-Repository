import flet as ft


def group(page: ft.Page):
    page.scroll = ft.ScrollMode.ALWAYS
    data = ft.Text(f"{page.client_storage.get("course_name")}")
    title = ft.Row([ft.Text(f"{data.value}'s group", size=36)])
    chat = ft.ListView(
        spacing=10,
        auto_scroll=True,
        padding=40,
        height=700,
        expand=True
    )
    group_participants = ["alex", "toni", "test"]

    def dropdown_handler(_):
        if _.data == "Private":
            friends_grid = ft.GridView(
                expand=50,
                runs_count=50,
                max_extent=50,
                child_aspect_ratio=0.5,
                spacing=50,
                run_spacing=50,
            )
            for participant in group_participants:
                friends_grid.controls.append(
                    ft.CupertinoCheckbox(
                        label=participant,
                    )
                )
            test_column.controls.append(
                ft.Text("Add participants", size=26),
            )
            test_column.controls.append(
                friends_grid
            )
            page.update()

    def close_dlg(e):
        creation_form.open = False
        page.update()

    def room_handler(_):
        page.dialog = creation_form
        creation_form.open = True
        page.update()

    test_column = ft.Column(
        controls=[
            ft.TextField(
                width=400,
                height=100,
                label="Room name",
                helper_text="Please enter your room name",
                bgcolor=ft.colors.BLACK45,
            ),
            ft.Dropdown(
                width=400,
                options=[
                    ft.dropdown.Option("Private"),
                    ft.dropdown.Option("Public"),
                ],
                on_change=dropdown_handler
            )
        ],
        height=500,
        width=500,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    creation_form = (ft.AlertDialog(
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
        modal=True,
        actions=[
            ft.TextButton("Create", on_click=close_dlg),
            ft.TextButton("Cancel", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        title=ft.Text("Study room creation"),
        content=test_column
    ))

    study_room_button = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(
                content=ft.ElevatedButton(
                    width=240,
                    height=40,
                    icon=ft.icons.HISTORY,
                    text="Create study room",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLACK45,
                    ),
                    on_click=room_handler
                )
            ),
            ft.PopupMenuItem(
                content=ft.ElevatedButton(
                    width=240,
                    height=40,
                    icon=ft.icons.HISTORY,
                    text="Assignments history",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLACK45,
                    ),
                )
            ),
        ],
    )

    def send_click(_):
        def remove_dialog(_):
            cupertino_alert_dialog.open = False
            page.update()

        cupertino_alert_dialog = ft.CupertinoAlertDialog(
            title=ft.Text("Invalid data"),
            content=ft.Text("Enter you message again."),
            actions=[
                ft.CupertinoDialogAction(
                    "OK",
                    is_destructive_action=True,
                    on_click=remove_dialog
                ),
                ft.CupertinoDialogAction(
                    text="Cancel",
                    on_click=remove_dialog
                ),
            ]
        )
        if new_message.value == "" or new_message.value == " ":
            page.dialog = cupertino_alert_dialog
            cupertino_alert_dialog.open = True
            page.update()
        else:
            chat.controls.append(
                ft.Container(
                    ft.Text(
                        f"/FIRST_NAME/: {new_message.value}",
                        size=20,
                    ),
                    padding=15,
                    border_radius=20,
                    bgcolor=ft.colors.BLUE_GREY,
                    expand=False,
                    width=100,
                )
            )
            new_message.value = ""
            page.update()

    new_message = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_click,
        border_radius=25
    )

    page.add(
        ft.Column(
            [ft.Row(
                [
                    title,
                ]
            ),
                ft.Row(
                    [
                        chat,
                    ],
                ),
                ft.Row(
                    [
                        new_message, study_room_button,
                    ]
                )],
            width=1600
        ),
    )
