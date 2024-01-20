from io import BytesIO

from fastapi import APIRouter, File, HTTPException, UploadFile

from ..color_extractor import extract_hsl_colors, extract_rgb_colors

router = APIRouter(prefix="/extract")

NUMBER_OF_COLORS = 5


@router.post("/rgb")
async def get_rgb_colors(image: UploadFile | None = None) -> list[dict[str, int]]:
    if not image:
        raise HTTPException(status_code=400, detail={"message": "No image file sent"})

    image_data = await image.read()
    return extract_rgb_colors(
        image_data=BytesIO(image_data), number_of_colors=NUMBER_OF_COLORS
    )


@router.post("/hsl")
async def get_hsl_colors(image: UploadFile | None = None) -> list[dict[str, int]]:
    if not image:
        raise HTTPException(status_code=400, detail={"message": "No image file sent"})

    image_data = await image.read()
    return extract_hsl_colors(
        image_data=BytesIO(image_data), number_of_colors=NUMBER_OF_COLORS
    )
