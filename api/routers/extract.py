from fastapi import APIRouter

from ..color_extractor import extract_hsl_colors, extract_rgb_colors

router = APIRouter(prefix="/extract")


@router.get("/rgb")
def get_rgb_colors() -> list[dict[str, int]]:
    return [{"message": 0}]


@router.get("/hsl")
def get_hsl_colors() -> list[dict[str, int]]:
    return [{"message": 1}]
