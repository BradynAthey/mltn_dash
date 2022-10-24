from io import BytesIO
import matplotlib.pyplot as plt
import base64

def mpl_fig_to_uri(fig, close_all=True, **save_args):
    """ encode a matplotlib figure as a URI """
    out_img = BytesIO()
    fig.savefig(out_img, format="png", **save_args)
    if close_all:
        fig.clf()
        plt.close("all")
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return "data:image/png;base64,{}".format(encoded)

