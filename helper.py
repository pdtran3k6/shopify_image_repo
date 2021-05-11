from PIL import Image
from typing import Optional

def conv_jpeg_to_jpg(file_ext: str) -> str:
  lowercased_file_ext = file_ext.lower()
  return lowercased_file_ext if lowercased_file_ext != 'jpeg' else 'jpg'

def validate_image(fullpath: str) -> Optional[str]:
    try:
        img_type = Image.open(fullpath).format
    except:
        print('Cannot get image type')
        return None
    return conv_jpeg_to_jpg(img_type)
