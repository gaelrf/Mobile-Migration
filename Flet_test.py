import os
import time
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):
    # test 1
    # page.title = "Flet counter example"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    # def minus_click(e):
    #     txt_number.value = str(int(txt_number.value) - 1)
    #     page.update()

    # def plus_click(e):
    #     txt_number.value = str(int(txt_number.value) + 1)
    #     page.update()

    # page.add(
    #     ft.Row(
    #         [
    #             ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
    #             txt_number,
    #             ft.IconButton(ft.icons.ADD, on_click=plus_click),
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER,
    #     )
    # )

    # test 2
    # t = ft.Text()
    # page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()
    # for i in range(10):
        # t.value = f"Step {i}"
        # page.update()
        # time.sleep(1)

    # test 3
    # for i in range(10):
    #     page.controls.append(ft.Text(f"Line {i}"))
    #     if i > 4:
    #         page.controls.pop(0)
    #     page.update()
    #     time.sleep(0.3)

    # test 4
    # def add_clicked(e):
    #     page.add(ft.Checkbox(label=new_task.value))
    #     new_task.value = ""
    #     new_task.focus()
    #     new_task.update()

    # new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    # page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    
    # test 5
    # first_name = ft.TextField()
    # last_name = ft.TextField()
    # c = ft.Column(controls=[
    #     first_name,
    #     last_name
    # ])
    # c.disabled = True
    # page.add(c)

    # test 6
    # first_name = ft.TextField(label="First name", autofocus=True)
    # last_name = ft.TextField(label="Last name")
    # greetings = ft.Column()

    # def btn_click(e):
    #     greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
    #     first_name.value = ""
    #     last_name.value = ""
    #     page.update()
    #     first_name.focus()

    # page.add(
    #     first_name,
    #     last_name,
    #     ft.ElevatedButton("Say hello!", on_click=btn_click),
    #     greetings,
    # )

    # test 7
    # lv = ft.ListView(expand=True, spacing=10)
    # for i in range(5000):
    #     lv.controls.append(ft.Text(f"Line {i}"))
    # page.add(lv)

    # test 8
    # r = ft.Row(wrap=True, scroll="always", expand=True)
    # page.add(r)

    # for i in range(5000):
    #     r.controls.append(
    #         ft.Container(
    #             ft.Text(f"Item {i}"),
    #             width=100,
    #             height=100,
    #             alignment=ft.alignment.center,
    #             bgcolor=ft.colors.AMBER_100,
    #             border=ft.border.all(1, ft.colors.AMBER_400),
    #             border_radius=ft.border_radius.all(5),
    #         )
    #     )
    # page.update()

    # test 9
    
    # # add ListView to a page first
    # lv = ft.ListView(expand=1, spacing=10, item_extent=50)
    # page.add(lv)

    # for i in range(5100):
    #     lv.controls.append(ft.Text(f"Line {i}"))
    #     # send page to a page
    #     if i % 500 == 0:
    #         page.update()
    # # send the rest to a page
    # page.update()

    # test 10

    page.title = "Drag and Drop example"

    def drag_accept(e):
        # get draggable (source) control by its ID
        src = page.get_control(e.src_id)
        # update text inside draggable control
        src.content.content.value = "0"
        # update text inside drag target control
        e.control.content.content.value = "1"
        page.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=ft.Text("1"),
                ),                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                ),
            ]
        )
    )

ft.app(target=main)
 