import imghdr

def conv_jpeg_to_jpg(file_ext):
  return file_ext if file_ext != 'jpeg' else 'jpg'

# using file header to ensure it's as the
# as the  extension in the filename
def validate_image(stream):
    # first 1024 bytes should be efficient to extract the header
    header = stream.read(1024)
    # reset seeker back to beginning of file
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return conv_jpeg_to_jpg(format)
