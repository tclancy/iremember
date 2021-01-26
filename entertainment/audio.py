from tempfile import NamedTemporaryFile

import pyttsx3


def text_to_temporary_file(text: str) -> NamedTemporaryFile:
    """
    Creates an AIFF file by default on Mac
    TODO: require a file path, use that. We can assume they will get overwritten regularly
    LATER: use caching to reduce thrashing

    TODO: play with voices, see if we can force an expected format for cross-platform
    """
    nt = NamedTemporaryFile()
    engine = pyttsx3.init()
    engine.save_to_file(text, nt.name)
    engine.runAndWait()
    return nt
