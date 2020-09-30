from settings import elements
from image import draw_element, img_concatenation, draw_link


def split(word):
    """
    This function parse word to Mendeleev elements
    :param word: word to parse  into Mendeleev elements
    :return: list of Mendeleev elements
    """
    word = word.lower()
    i = 0
    imgs = []
    while i < len(word):
        if i < len(word) - 1:
            if word[i:i + 2] in elements:
                imgs.append(elements[word[i:i + 2]])
                i += 2
            else:
                imgs.append(elements[word[i]])
                i += 1
        else:
            imgs.append(elements[word[i]])
            i += 1

    return imgs


def make_jpg(imgs):
    """
    This function makes result photo
    :param imgs: list of Mendeleev elements
    :return: result photo
    """
    b = []
    for img in imgs:
        b.append(draw_element(img))
    return draw_link(img_concatenation(b))
