import flet as ft
import requests
from content_page import content
from courses_pick_page import courses_pick
import json


def authentication(page: ft.Page) -> any:
    page.title = "Autnentication"
    page.window_maximized = True
    page.window_resizable = False
    page.bgcolor = "#222B28"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50

    def login_redirection(_):
        page.clean()
        login_form_setup()

    def registration_redirection(_):
        page.clean()
        registration_form_setup()

    def login_form_setup() -> ft.Column:
        def validate_form(_) -> any:
            if not email.value:
                email.error_text = "Email cant be empty"
                email.update()
            elif not password.value:
                password.error_text = "Password cant be empty"
                password.update()
            else:
                data = {
                    "email": email.value,
                    "password": password.value
                }
                login_request = requests.post(
                    url="http://127.0.0.1:4000/api/auth",
                    json=data
                )
                if login_request.status_code == 200:
                    token = json.loads(login_request.text)
                    page.clean()
                    page.client_storage.set("token", token["token"])
                    content(page)
                else:
                    page.dialog = cupertino_alert_dialog
                    cupertino_alert_dialog.open = True
                    page.update()

        form_fields = []

        logotype = ft.Image(
            src="https://i.ibb.co/jHj12vJ/bisonspace-logo-2.png",
            width=600,
            height=200,
        )
        email = ft.TextField(
            width=400,
            height=100,
            label="Email",
            helper_text="Please enter your email",
            bgcolor=ft.colors.BLACK45,
            keyboard_type=ft.KeyboardType.EMAIL
        )
        password = ft.TextField(
            width=400,
            height=100,
            label="Password",
            helper_text="Please enter your password",
            bgcolor=ft.colors.BLACK45,
            password=True,
            can_reveal_password=True
        )
        buttons = ft.Row(
            [
                ft.ElevatedButton(
                    width=100,
                    height=40,
                    text="Login",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLACK45,
                    ),
                    on_click=validate_form
                ),
                ft.TextButton(
                    text="You do nat have account? Register",
                    width=300,
                    on_click=registration_redirection
                ),
            ]
        )

        form_fields.append(logotype)
        form_fields.append(email)
        form_fields.append(password)
        form_fields.append(buttons)

        form_container = ft.Column(
            height=900,
            spacing=20,
            controls=form_fields,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        page.add(ft.Row(
            [form_container, ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ))

        def remove_dialog(_):
            cupertino_alert_dialog.open = False
            email.value = None
            password.value = None
            page.update()

        cupertino_alert_dialog = ft.CupertinoAlertDialog(
            title=ft.Text("Invalid data"),
            content=ft.Text("Enter you data again."),
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

        return form_container

    def registration_form_setup() -> any:
        def validate_form(_) -> any:
            if not first_name.value:
                first_name.error_text = "First name cant be empty"
                first_name.update()
            if not last_name.value:
                last_name.error_text = "Last name cant be empty"
                last_name.update()
            if not email.value:
                email.error_text = "Email cant be empty"
                email.update()
            elif not password.value:
                password.error_text = "Password cant be empty"
                password.update()
            else:
                data = {
                    "firstName": first_name.value,
                    "lastName": last_name.value,
                    "email": email.value,
                    "password": password.value
                }
                registration_request = requests.post(
                    url="http://127.0.0.1:4000/api/users",
                    json=data
                )
                if registration_request.status_code == 201:
                    token = json.loads(registration_request.text)
                    page.clean()
                    page.client_storage.set("token", token["token"])
                    courses_pick(page)
                    page.update()
                else:
                    page.dialog = cupertino_alert_dialog
                    cupertino_alert_dialog.open = True
                    page.update()

        form_fields = []

        logotype = ft.Image(
            src="https://i.ibb.co/jHj12vJ/bisonspace-logo-2.png",
            width=600,
            height=200,
        )
        first_name = ft.TextField(
            width=400,
            height=100,
            label="First name",
            helper_text="Please enter your first name",
            bgcolor=ft.colors.BLACK45,
            keyboard_type=ft.KeyboardType.EMAIL
        )
        last_name = ft.TextField(
            width=400,
            height=100,
            label="Last name",
            helper_text="Please enter your last name",
            bgcolor=ft.colors.BLACK45,
            keyboard_type=ft.KeyboardType.EMAIL
        )
        email = ft.TextField(
            width=400,
            height=100,
            label="Email",
            helper_text="Please enter your email",
            bgcolor=ft.colors.BLACK45,
            keyboard_type=ft.KeyboardType.EMAIL
        )
        password = ft.TextField(
            width=400,
            height=100,
            label="Password",
            helper_text="Please enter your password",
            bgcolor=ft.colors.BLACK45,
            password=True,
            can_reveal_password=True
        )
        buttons = ft.Row(
            [
                ft.ElevatedButton(
                    width=110,
                    height=40,
                    text="Register",
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.BLACK45,
                    ),
                    on_click=validate_form
                ),
                ft.TextButton(
                    text="You do nat have account? Login",
                    width=300,
                    on_click=login_redirection
                ),
            ]
        )

        form_fields.append(logotype)
        form_fields.append(first_name)
        form_fields.append(last_name)
        form_fields.append(email)
        form_fields.append(password)
        form_fields.append(buttons)

        form_container = ft.Column(
            height=900,
            spacing=20,
            controls=form_fields,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        def remove_dialog(_):
            cupertino_alert_dialog.open = False
            email.value = None
            password.value = None
            page.update()

        cupertino_alert_dialog = ft.CupertinoAlertDialog(
            title=ft.Text("Invalid data"),
            content=ft.Text("Enter you data again."),
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

        page.add(ft.Row(
            [form_container, ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ))

    page.add(ft.Row(
        [login_form_setup(), ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    ))


ft.app(target=authentication, )
