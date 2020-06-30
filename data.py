from skimage import io
import os


def read_texs():
    """
    Compiles a dict with the format filename:image
    for all the textures in the /textures folder
    """
    texs = {}
    d = os.path.dirname(os.path.realpath(__file__))
    tex_path = os.path.join(d, "textures")
    for filename in os.listdir(tex_path):
        name = filename.split(".")[0]
        texs[name] = io.imread(fname=os.path.join(
            tex_path, filename), as_gray=True)
    return texs
