import colorgram


def extract_rgb_colors(image: str, number_of_colors: int) -> list[dict[str, int]]:
    colors = colorgram.extract(image, number_of_colors)
    return [color.rgb._asdict() for color in colors]


def extract_hsl_colors(image: str, number_of_colors: int) -> list[dict[str, int]]:
    colors = colorgram.extract(image, number_of_colors)
    return [color.hsl._asdict() for color in colors]
