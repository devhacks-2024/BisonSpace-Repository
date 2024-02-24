import flet as ft
import requests


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
    group_participants = ["alex", "toni", "test", "alex", "toni", "test", "alex", "toni", "test", "alex", "toni",
                          "test", "alex", "toni", "test", "alex", "toni", "test"]
    selected_participants = []
    room_type = ""

    def next_window_handler(_):
        # data = {
        #     "course": page.client_storage.get("course_name"),
        #     "user": selected_participants,
        #     "type": room_type,
        # }
        # room_request = requests.post(
        #     url="http://127.0.0.1:4000:URL",
        #     json=data
        # )
        status_code = 200
        if status_code == 200:
            creation_form.open = False
            page.dialog = None
            page.update()

            assignment_form.open = True
            page.dialog = assignment_form
            page.update()

    def checkbox_handler(_):
        if _.data == "true":
            selected_participants.append(_.control.label)
        elif _.data == "false":
            selected_participants.remove(_.control.label)

    def dropdown_handler(_):
        if _.data == "Private":
            friends_grid = ft.GridView(
                expand=50,
                runs_count=50,
                max_extent=50,
                child_aspect_ratio=1.0,
                spacing=10,
                run_spacing=30,
                width=400
            )
            for participant in group_participants:
                friends_grid.controls.append(
                    ft.CupertinoCheckbox(
                        label=participant,
                        on_change=checkbox_handler
                    )
                )
            room_column.controls = [
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
                ),
                ft.Text("Add participants", size=26),
                friends_grid
            ]
            room_type = "Private"
            page.update()
        elif _.data == "Public":
            room_type = "Public"
            room_column.controls = [
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
                ),
                ft.Text(
                    "Type: Public"
                )
            ]
            page.update()

    def close_dlg(e):
        creation_form.open = False
        page.update()

    def close_assignment(e):
        assignment_form.open = False
        page.update()

    def room_handler(_):
        page.dialog = creation_form
        creation_form.open = True
        page.update()

    room_column = ft.Column(
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
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    assignment_name = ft.TextField(
        width=400,
        height=100,
        label="Assignment name",
        helper_text="Please enter your assignment name",
        bgcolor=ft.colors.BLACK45,
    )

    assignment_description = ft.TextField(
        width=400,
        height=100,
        label="Description",
        helper_text="Please enter your description",
        bgcolor=ft.colors.BLACK45,
    )

    assignment_dropdown = ft.Dropdown(
        width=400,
        options=[
            ft.dropdown.Option("Python"),
            ft.dropdown.Option("Java"),
            ft.dropdown.Option("Plain text"),
        ],
    )

    def assignment_button_handler(_):
        if assignment_name.value == "" or assignment_description.value == "":
            page.dialog = cupertino_alert_dialog
            cupertino_alert_dialog.open = True
            page.update()
        else:
            try:
                if assignment_dropdown.value == "Python":
                    fp = open(f'frontend/assignments/{str(assignment_name.value).replace(" ", "")}.py', 'x')
                    fp.close()
                    print("Python is created")
                elif assignment_dropdown.value == "Java":
                    fp = open(f'frontend/assignments/{str(assignment_name.value).replace(" ", "")}.java', 'x')
                    fp.close()
                    print("Java is created")
                elif assignment_dropdown.value == "Plain text":
                    fp = open(f'frontend/assignments/{str(assignment_name.value).replace(" ", "")}.txt', 'x')
                    fp.close()
                    print("txt is created")
                else:
                    fp = open(f'frontend/assignments/{str(assignment_name.value).replace(" ", "")}.txt', 'x')
                    fp.close()
                    print("txt is created")
            except FileExistsError:
                page.dialog = cupertino_alert_dialog
                cupertino_alert_dialog.open = True
                page.update()

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

    assignment_button = ft.ElevatedButton(
        width=240,
        height=40,
        icon=ft.icons.HISTORY,
        text="Create assignment",
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLACK45,
        ),
        on_click=assignment_button_handler
    )

    assignment_column = ft.Column(
        controls=[assignment_name, assignment_description,
                  assignment_dropdown],
        height=500,
        width=500,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    creation_form = (ft.AlertDialog(
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
        modal=True,
        actions=[
            ft.TextButton("Next", on_click=next_window_handler),
            ft.TextButton("Cancel", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        title=ft.Text("Study room creation"),
        content=room_column
    ))

    assignment_form = (ft.AlertDialog(
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
        modal=True,
        actions=[
            assignment_button,
            ft.TextButton("Cancel", on_click=close_assignment),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        title=ft.Text("Study room creation"),
        content=assignment_column
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
