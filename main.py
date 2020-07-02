import data
import synthesis as s
import time
import matplotlib.pyplot as plt


def run(texs):
    new_texs = {}
    for i, tex_name in enumerate(texs):
        new_imgs = []
        for j, size in enumerate(data.WIN_SIZES):
            print(f"Starting synthesis for {tex_name} w={size}")
            start = time.perf_counter()
            new_img = s.synthesis(
                texs[tex_name], data.NEW_IMG_SIZE, size, data.GAUSS_MASKS[j])
            print(f"Finished synthesis in {time.perf_counter() - start}s")
            new_imgs.append(new_img)
        new_texs[tex_name] = new_imgs
    return new_texs


def plot(texs, syns):
    fig, axs = plt.subplots(len(texs), len(
        data.WIN_SIZES) + 1, constrained_layout=True)
    fig.suptitle(f"Texture synthesis results w={data.WIN_SIZES}")
    for i, name in enumerate(texs):
        if len(texs) > 1:
            orig_ax, axs = axs[i, 0], axs[i, 1:]
        else:
            orig_ax, axs = axs[0], axs[1:]

        orig_ax.set_title(f"{name} Texture Original")
        orig_ax.imshow(texs[name], cmap="gray")

        for j, size in enumerate(data.WIN_SIZES):
            axs[j].set_title(f"{name} Texture Synthesized W={size}")
            axs[j].imshow(syns[name][j], cmap="gray")

    plt.show()


if __name__ == "__main__":
    # Reads all imgs in /textures folder
    print("* STARTING READ *")
    TEXS = data.read_texs()
    print("* STARTING SYNTHESIS *")
    SYNS = run(TEXS)
    print("* STARTING PLOTTING *")
    plot(TEXS, SYNS)
    print("* DONE *")
