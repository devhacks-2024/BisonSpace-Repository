import flet as ft
from sockets import socket


def assignment(page: ft.Page):

    socket.emit("join_studyRoom", page.client_storage.get("roomId"))
    page.scroll = ft.ScrollMode.ALWAYS

    key_words = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
                 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
                 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield', "True:",
                 "if(", ")"]

    preview_column = ft.Column(
        spacing=1,
        width=500,
        height=800,
        scroll=ft.ScrollMode.ALWAYS,
        controls=[]
    )

    def send_and_get_data(_):
        preview_column.controls = []
        data = code_column.value.split("\n")
        for i in data:
            result = ft.Row(
                controls=[],
                width=100,
                height=16
            )
            spl = i.split(" ")
            for n in spl:
                if n in key_words:
                    tt = ft.Text(f"{n}", color=ft.colors.BLUE)
                    result.controls.append(tt)
                else:
                    tt = ft.Text(f"{n}", color=ft.colors.WHITE)
                    result.controls.append(tt)
            preview_column.controls.append(result)
            page.update()

    code_column = ft.TextField(
        width=700,
        height=800,
        multiline=True,
        min_lines=15,
        color=ft.colors.BLACK45,
        bgcolor=ft.colors.GREEN_100,
        on_change=send_and_get_data
    )

    chat_column = ft.Column(
        width=500,
        height=800
    )
    page.add(ft.Row(
        controls=[
            code_column, preview_column, chat_column
        ],
    ))

    while True:
        events = socket.receive()
        print(events)
        # if events[0] == "studyRoomAssignment":

        # code_column.value = events[1:][0]
        #     pass
        page.update()


