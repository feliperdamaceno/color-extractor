from io import BytesIO

import colorgram


def extract_rgb_colors(
    image_data: BytesIO, number_of_colors: int
) -> list[dict[str, int]]:
    colors = colorgram.extract(image_data, number_of_colors)
    return [color.rgb._asdict() for color in colors]
