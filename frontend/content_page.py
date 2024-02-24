import flet as ft


def content(page: ft.Page) -> any:
    page.title = "Content"

    def tab_handler(tab):
        if tab.data == "0":
            page.clean()
            pass
            page.update()
        elif tab.data == "1":
            page.clean()
            pass
            page.update()
        elif tab.data == "2":
            page.clean()
            pass
            page.update()

    page.navigation_bar = ft.NavigationBar(
        on_change=tab_handler,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.STORAGE_OUTLINED, label="My courses"),
            ft.NavigationDestination(icon=ft.icons.GROUPS, label="Chats"),
            ft.NavigationDestination(icon=ft.icons.SD_STORAGE, label="Storage"),
            ft.NavigationDestination(
                icon=ft.icons.PERSON,
                selected_icon=ft.icons.BOOKMARK,
                label="Profile",
            ),
        ]
    )
    page.add()
