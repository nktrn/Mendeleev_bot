from settings import WIDTH, HEIGHT, BLACK, FONT_URL_REGULAR, FONT_URL_BOLD, FONT_NAME_SIZE, FONT_INDEX_SIZE, \
    FONT_FULLNAME_SIZE, OFFSET, elements
from PIL import Image, ImageDraw, ImageFont


def draw_element(element):
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


def img_concatenation(imgs):
    total_width = len(imgs) * WIDTH

    new_im = Image.new('RGB', (total_width, HEIGHT))

    x_offset = 0

    for im in imgs:
        new_im.paste(im, (x_offset, 0))
        x_offset += WIDTH + OFFSET

    return new_im


class Generate:
    def __init__(self, word=None, user_id=None):
        self.word = word.lower()
        self.name_file = word
        self.separated_elements = []
        self.user_id = user_id
        self.imgs = []

    def split(self):
        i = 0
        while i < len(self.word):
            if i < len(self.word) - 1:
                if self.word[i:i + 2] in elements:
                    self.imgs.append(elements[self.word[i:i + 2]])
                    i += 2
                else:
                    self.imgs.append(elements[self.word[i]])
                    i += 1
            else:
                self.imgs.append(elements[self.word[i]])
                i += 1

    def make_jpg(self):
        b = []
        for img in self.imgs:
            b.append(draw_element(img))
        return img_concatenation(b)
