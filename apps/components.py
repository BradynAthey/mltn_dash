import dash_cytoscape as cyto


def get_static_image(src, width="100%"):
    return html.Img(src=src, width=width)


def get_cyto_graph(
    elements,
    id="cyto-graph",
    layout={"name": "circle", "directed": "true", "radius": 1000},
    style={"height": "80vh", "width": "100%"},
):

    if isinstance(elements, str):
        # assume filepath to json elements definition
        with open(elements, "r") as f:
            elements = json.load(f)
    else:
        if not isinstance(elements, list):
            raise ValueError(
                "`elements` must be a list of graph elements or a filepath (string) to elements in json"
            )

    stylesheet = stylesheet or [
        {
            "selector": "node",
            "style": {
                "label": "data(label)",
                "width": "350%",
                "height": "350%",
                "text-wrap": "wrap",
                "text-valign": "center",
                "text-halign": "center",
                "text-max-width": "60px",
                "color": "white",
                "font-size": "55px",
            },
        },
        {
            "selector": "edge",
            "style": {
                "width": "3px",
                "target-arrow-shape": "triangle",
                "source-arrow-shape": "triangle",
                "curve-style": "bezier",
                "label": "data(label)",
                "edge-text-rotation": "autorotate",
                "font-size": "40px",
                "control-point-step-size": "100px",
            },
        },
    ]

    return cyto.Cytoscape(
        id=id,
        layout=layout,
        style=style,
        minZoom=0.1,
        maxZoom=1,
        elements=elements,
        stylesheet=stylesheet,
    )
