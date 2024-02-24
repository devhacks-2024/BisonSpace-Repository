import flet as ft
from groups_page import groups
import requests
from sockets import connect
from profile_page import profile


def content(page: ft.Page) -> any:
    connect("http://127.0.0.1:4000", page.client_storage.get("token"))

    page.title = "Content"
    user_information_request = requests.get(
        url="http://127.0.0.1:4000/api/users",
        headers={"authorization": f"{page.client_storage.get('token')}"}
    )
    user_information = user_information_request.json()

    page.client_storage.set("user_id", user_information["user"]["_id"])
    page.client_storage.set("user_first_name", user_information["user"]["firstName"])
    page.client_storage.set("user_last_name", user_information["user"]["lastName"])
    page.client_storage.set("user_default_color", user_information["user"]["defaultProfileColor"])

    groups(page)

    def tab_handler(tab):
        if tab.data == "0":
            page.clean()
            groups(page)
            page.update()
        elif tab.data == "1":
            page.clean()
            profile(page)
            page.update()

    page.navigation_bar = ft.NavigationBar(
        on_change=tab_handler,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.STORAGE_OUTLINED, label="My courses"),
            ft.NavigationDestination(
                icon=ft.icons.PERSON,
                selected_icon=ft.icons.BOOKMARK,
                label="Profile",
            ),
        ]
    )
    page.add()
