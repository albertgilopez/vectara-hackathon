import logging
import sys

# Configuración global del logger
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
# logger = logging.getLogger(__name__)

# 1. Inicializar configuración
# 2. Definir funciones y clases
# 3. Controlar el flujo del programa
# 4. Manejar excepciones y errores
# 5. Ejecutar la lógica principal del programa
# 6. Finalizar o limpiar recursos

import reflex as rx

from .helpers import navbar
from vectara.state import State

from vectara.components import feedback

def home():
    return rx.center(
        navbar(State),
        rx.vstack(
            rx.center(
                 rx.vstack(
                    rx.form(
                        rx.form_control(
                            rx.vstack(
                                rx.heading("Ask Vectara DOCS", font_size="1.5em"),

                                rx.input(
                                on_blur=State.set_prompt, placeholder="Escribe aquí tu pregunta", width="100%"
                                ),

                                rx.button(
                                    rx.text("Preguntar"),
                                    rx.cond(
                                        State.processing,
                                        rx.text("Preguntar"),
                                    ),
                                    type_="submit",
                                    is_loading=State.processing,
                                    loading_text="Generando la respuesta. Un momento, por favor.",
                                    spinner_placement="start",
                                    width="100%"
                                ),

                            ),
                            is_disabled=State.processing,
                        ),
                        on_submit=State.get_result,
                        width="100%",
                        
                        spacing="2em",
                        padding_top="6em",
                        text_align="top",
                        position="relative",
                        bottom="0",
                        left="0",
                        py="4",
                        backdrop_filter="auto",
                        backdrop_blur="lg",
                        align_items="stretch",
                    ),

                    rx.text_area(
                        default_value=State.result,
                        placeholder="Aquí se motrará la respuesta",
                        width="100%",
                        
                    ),

                    rx.text(
                        "Ask GPT puede generar respuestas incorrectes o incompletas. Revisa el contenido que genera.",
                        font_size="xs",
                        text_align="left",
                    ),
                    
                    rx.vstack(
                        rx.cond(
                            State.checked,
                            rx.text("Ocultar detalles", color="red", font_size="small"),
                            rx.text("Ver detalles", color="green", font_size="small"),
                        ),
                        rx.debounce_input(
                        
                            rx.checkbox(
                                on_change=State.set_checked,
                            
                            ),
                            on_click=State.toggle_feedback,
                            debounce_timeout=500,
                            
                        ),
                        
                    ),

                    feedback.give_feedback(State),
                        
                    rx.button("Guardar Respuesta", on_click=State.save_result, width="100%"),
                    
                    shadow="lg",
                    padding="1em",
                    border_radius="lg",
                    width="100%",
                 ),
                 
                 width="100%",
                 
            ),
                            rx.center(
                                rx.vstack(
                                    rx.heading("Historial", font_size="1.5em"),
                                    rx.divider(),
                                    rx.data_table(
                                        data=State.questions,
                                        # columns=["Question", "Answer"],
                                        columns=State.show_columns,
                                        pagination=True,
                                        search=True,
                                        sort=True,
                                        width="100%",
                                    ),
                                    shadow="lg",
                                    padding="1em",
                                    border_radius="lg",
                                    width="100%",
                                ),
                                width="100%",
                            
                            ),
                            
                            width="50%",
                            spacing="2em",
                            
                        ),
                            
                            padding_top="6em",
                            text_align="top",
                            position="relative",
        
    )

def login():
    return rx.center(
        rx.vstack(
            rx.input(on_blur=State.set_username, placeholder="Usuario", width="100%"),
            rx.input(type_="password", on_blur=State.set_password, placeholder="Contraseña", width="100%"),
            rx.button("Iniciar Sesión", on_click=State.login, width="100%"),
            rx.link(rx.button("Registrarse", width="100%"), href="/signup", width="100%"),
        ),
        shadow="lg",
        padding="1em",
        border_radius="lg",
        background="white",
    )


def signup():
    return rx.box(
        rx.vstack(
            rx.center(
                rx.vstack(
                    rx.heading("Crear una cuenta", font_size="1.5em"),
                    rx.input(
                        on_blur=State.set_username, placeholder="Escribe un nombre de usuario", width="100%"
                    ),
                    rx.input(
                        type_="password", on_blur=State.set_password, placeholder="Escribe una contraseña", width="100%"
                    ),
                    rx.input(
                        type_="password",
                        on_blur=State.set_password,
                        placeholder="Vuelve a escribir la contraseña",
                        width="100%",
                    ),
                    rx.button("Registrarse", on_click=State.signup, width="100%"),
                ),
                shadow="lg",
                padding="1em",
                border_radius="lg",
                background="white",
            )
        ),
        padding_top="10em",
        text_align="top",
        position="relative",
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )


def index():

    return rx.box(
        rx.vstack(
            navbar(State),
            login(),
        ),
       
        padding_top="10em",
        text_align="top",
        position="relative",
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.add_page(signup)
app.add_page(home)
# app.add_page(detalles_feedback)

app.compile()

