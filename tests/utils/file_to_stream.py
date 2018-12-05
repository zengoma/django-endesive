import io


def file_to_stream(file_object):
    """Ability to get file from stream instead of hard disk

    :param file_object:
    :return: BytesIO stream
    """
    buffer = io.BytesIO(file_object)
    stream = buffer.getvalue()
    buffer.close()
    return stream
