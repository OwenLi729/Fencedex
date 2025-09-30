"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

#okay system design
#website: reflex
#backend db: Postgresql
#security & testing for workers: Hatchet
#APIs? graphql, postman api testing, etc. systems & design
#JSON, SQL
#auth with
#data cleaning & inconsistencies
#SWS done now need MS, MF, ME, WF, WE
#not all bouts included (Heraklion excluded for WS)

#create title, logo, search feature (rudimentary)

#service key for backend tasks in .env file

class State(rx.State):
    """The app state."""
    '''
    @rx.event
    def show_main(self):
        self.set_route("main") 
    '''
    fencer_selected: bool = False
    tournament_selected: bool = False

    def select_fencer(self):
        self.fencer_selected = True
        self.tournament_selected = False
    def select_tournament(self):
        self.tournament_selected = True
        self.fencer_selected = False
    def find_tournament(self):
        return
        # logic for finding a tournament from supabase DB
    def find_fencer(self):
        return
        # logic for finding a fencer from supabase DB
    def find_bout(self):
        return
        # logic for finding a specific bout. Input fields: gender, weapon, tournament (with date), fencer 1, fencer 2, event (team, individual)
#class ClickState(rx.State):

    


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.box(
                rx.heading("Welcome to Fendex!", size="9", margin_bottom="40px", margin_top="100px"),
                rx.text(
                    "Your one-stop destination for browsing tournament history ",
                    size="5",
                    margin_bottom="80px"
                ),
                # Need to fix link logic
                rx.link(
                rx.button(
                        "Get started", 
                        on_click=rx.redirect(
                            "/main",
                            is_external=False,
                        ),
                    ),
                    spacing="5",
                    justify="center",
                    min_height="85vh",
                ),
                padding="10px",
            ),
            
            spacing="9",
        )
    )

def main_page() -> rx.Component:

    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.box(
                rx.heading("Search", size="9", margin_bottom="40px", margin_top="80px"),
                rx.text("Filter based on individual or tournament history", size="5", margin_bottom="40px"),
            ),

            rx.menu.root(
                rx.menu.trigger(
                    rx.button("Select", variant="soft"),
                ),
                rx.menu.content(
                    rx.menu.item("Fencer History", on_click=State.select_fencer),
                    rx.menu.item("Tournament History", on_click=State.select_tournament),
                ),

            ),

            # Search bar by individual fencer
            rx.box(
                rx.cond(
                    State.fencer_selected,
                    rx.menu.root(
                        rx.menu.trigger(rx.button("Open Menu")), # fix
                        rx.menu.content(
                            rx.menu.item("Select fencer", on_click=State.find_fencer),
                            # then add fencers
                            # after a fencer is selected, it should open a new page (views) with a quick summary of the fencer and all their bouts on the sidebar with option to select specific opponents, after that on the right there should be option to view video
                        )
                    ),
                ),
            ),

            # Search bar by tournament
            rx.box(
                rx.cond(
                    State.tournament_selected,
                    rx.menu.root(
                        rx.menu.trigger(rx.button("Open Menu")), # fix
                        rx.menu.content(
                            rx.menu.item("Select tournament", on_click=State.find_tournament),
                            # then add fencers
                            # tournament selection should involve searching (with auto update live) by season, tournament name, gender, weapon, event and then after the user selects a tournament, it should give them a table with all the bouts. They should be able to select a specific bout from the bout table and preview it
                        )
                    ),
                ),
            )
        )
    ) 


def admin_page() -> rx.Component:
    # Admin Page (Monitor)
    return

#main vs main# routing error
app = rx.App()
app.add_page(index, route="/") #route
app.add_page(main_page, route="/main")
#views
