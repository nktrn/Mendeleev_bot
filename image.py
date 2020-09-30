from PIL import Image, ImageDraw, ImageFont
from settings import WIDTH, HEIGHT, BLACK, FONT_URL_REGULAR, FONT_URL_BOLD, FONT_NAME_SIZE, FONT_INDEX_SIZE, \
    FONT_FULLNAME_SIZE, OFFSET, URL, FONT_BOT_URL_SIZE


def draw_element(element):
    """
    This function draw an Mendeleev element
    :param element: Mendeleev element need to draw
    :return: Mendeleev element Image
    """
    image = Image.new("RGB", (WIDTH, HEIGHT), element.color)
    draw = ImageDraw.Draw(image)

    # draw index
    font = ImageFont.truetype(FONT_URL_BOLD, size=FONT_INDEX_SIZE)
    size = font.getsize(str(element.index))
    draw.text((WIDTH / 2 - size[0] / 2, HEIGHT / 15), str(element.index), fill=BLACK, font=font)

    # draw name
    font = ImageFont.truetype(FONT_URL_BOLD, size=FONT_NAME_SIZE)
    size = font.getsize(element.name)
    draw.text((WIDTH / 2 - size[0] / 2, HEIGHT / 4), element.name, fill=BLACK, font=font)

    # draw fullname
    font = ImageFont.truetype(FONT_URL_REGULAR, size=FONT_FULLNAME_SIZE)
    size = font.getsize(element.fullname)
    draw.text((WIDTH / 2 - size[0] / 2, 3 * HEIGHT / 4), element.fullname, fill=BLACK, font=font)

    return image


def draw_link(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_URL_REGULAR, size=FONT_BOT_URL_SIZE)
    size = font.getsize(URL)
    draw.text((OFFSET * 2, HEIGHT - size[1] - OFFSET * 2), URL, fill=BLACK, font=font)

    return img


def img_concatenation(imgs):
    """
    This function concatenates list of images into one image
    :param imgs:  list of images
    :return: image
    """
    total_width = len(imgs) * WIDTH

    new_im = Image.new('RGB', (total_width, HEIGHT))

    x_offset = 0

    for im in imgs:
        new_im.paste(im, (x_offset, 0))
        x_offset += WIDTH + OFFSET

    return new_im
