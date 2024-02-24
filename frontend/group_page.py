import flet as ft
from assignment_page import assignment
import requests
from avatar_generator import generator


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
    group_participants_request = requests.get(
        url=f"http://127.0.0.1:4000/api/courses/{page.client_storage.get("course_id")}/users",
        headers={"authorization": f"{page.client_storage.get('token')}"}
    )
    group_participants = group_participants_request.json()
    selected_participants = []

    def next_window_handler(_):
        data = {
            "type": page.client_storage.get("room_type"),
            "users": selected_participants,
            "name": "some test",
            "courseId": page.client_storage.get("course_id"),
        }
        room_request = requests.post(
            url="http://127.0.0.1:4000/api/studyRoom",
            json=data,
            headers={"authorization": f"{page.client_storage.get('token')}"}
        )
        if room_request.status_code == 201:
            page.close_dialog()
            creation_form.open = False
            page.update()
            page.dialog = assignment_form
            assignment_form.open = True
            page.update()

    def checkbox_handler(_):
        if _.data == "true":
            selected_participants.append(_.control.label)
        elif _.data == "false":
            selected_participants.remove(_.control.label)

    def dropdown_handler(_):
        if _.data == "Private":
            friends_grid = ft.ListView(
                expand=10,
                spacing=10,
                width=400
            )
            for participant in group_participants["users"]:
                if participant["_id"] != page.client_storage.get("user_id"):
                    friends_grid.controls.append(
                        ft.CupertinoCheckbox(
                            label=f"{participant["firstName"]} {participant["lastName"]}",
                            on_change=checkbox_handler
                        )
                    )
                else:
                    pass
            room_column.controls = [
                room_dropdown,
                room_name,
                ft.Text("Add participants", size=26),
                friends_grid
            ]
            page.client_storage.set("room_type", "private")
            page.update()
        elif _.data == "Public":
            page.client_storage.set("room_type", "public")
            room_column.controls = [
                room_dropdown,
                room_name,
                ft.Text(
                    "Type: Public",
                    size=18
                )
            ]
            page.update()

    def close_dlg(e):
        page.close_dialog()
        creation_form.open = False
        page.update()

    def room_handler(_):
        page.dialog = creation_form
        creation_form.open = True
        page.update()

    room_name = ft.TextField(
        width=400,
        height=100,
        label="Room name",
        helper_text="Please enter your room name",
        bgcolor=ft.colors.BLACK45,
    )
    room_dropdown = ft.Dropdown(
        width=400,
        options=[
            ft.dropdown.Option("Private"),
            ft.dropdown.Option("Public"),
        ],
        on_change=dropdown_handler
    )

    room_column = ft.Column(
        controls=[
            room_dropdown,
            room_name
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
        try:
            if assignment_dropdown.value == "Python":
                fp = open(f'frontend/assignments/{str(assignment_name.value).replace(" ", "")}.py', 'x')
                fp.close()
                page.close_dialog()
                assignment_form.open = False
                page.update()
                page.clean()
                assignment(page)
                page.update()
            elif assignment_dropdown.value == "Java":
                fp = open(f'frontend/assignments/{str(assignment_name.value).replace(" ", "")}.java', 'x')
                fp.close()
                page.close_dialog()
                assignment_form.open = False
                page.update()
                page.controls.clear()
                assignment(page)
                page.update()
            elif assignment_dropdown.value == "Plain text":
                fp = open(f'frontend/assignments/{str(assignment_name.value).replace(" ", "")}.txt', 'x')
                fp.close()
                page.close_dialog()
                assignment_form.open = False
                page.update()
                page.clean()
                assignment(page)
                page.update()
            else:
                fp = open(f'frontend/assignments/{str(assignment_name.value).replace(" ", "")}.txt', 'x')
                fp.close()
                page.close_dialog()
                assignment_form.open = False
                page.update()
                page.clean()
                assignment(page)
                page.update()
        except FileExistsError:
            page.dialog = cupertino_alert_dialog
            cupertino_alert_dialog.open = True
            page.update()

    def remove_dialog(_):
        page.close_dialog()
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
            ft.TextButton("Submit", on_click=assignment_button_handler),
            ft.TextButton("Cancel", on_click=close_dlg),
        ],
        title=ft.Text("Assignment form"),
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

    generated_avatar = generator(
        first_name=page.client_storage.get("user_first_name"),
        last_name=page.client_storage.get("user_last_name"),
        default_color=page.client_storage.get("user_default_color")
    )

    def send_click(_):
        if new_message.value == "" or new_message.value == " ":
            page.dialog = cupertino_alert_dialog
            cupertino_alert_dialog.open = True
            page.update()
        else:
            chat.controls.append(
                ft.Container(
                    ft.Row([generated_avatar, ft.Text(
                        f"{page.client_storage.get("user_first_name")}: {new_message.value}",
                        size=20,
                    ), ]),
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
