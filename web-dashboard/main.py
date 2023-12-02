from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.main import create_main_layout


def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "my Dashboard"
    app.layout = create_main_layout(app)
    app.run()


if __name__ == "__main__":
    main()
