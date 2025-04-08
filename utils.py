import pyautogui

from functools import wraps
from PIL import ImageFile
from time import sleep, time
from typing import Callable


def count_execution_time(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        total_time = time() - start_time
        print(f"Execution took {total_time} seconds")
        return result
    return wrapper


def locate_with_tries(element: ImageFile, *, tries: int = 1, **kwargs):
    """Try to locate element on the screen.

    Args:
        element (PIL.ImageFile): Image opened with PIL.
        tries (int, optional): Number of tries to find the element.
            Set -1 to look for the element until found.
            Defaults to 1.
    """

    current_try = 0

    confidence = kwargs.get("confidence", 0.9)

    if tries == -1:
        while True:
            # look for the element until found
            try:
                coords = pyautogui.locateOnScreen(element, confidence=confidence)
                if coords:
                    return coords
            except pyautogui.ImageNotFoundException as e:
                sleep(0.5)

    for _ in range(tries):
        sleep(0.3)
        try:
            coords = pyautogui.locateOnScreen(element, confidence=confidence)
            if coords:
                return coords
        except pyautogui.ImageNotFoundException as e:
            current_try += 1
            if current_try != tries - 1:
                sleep(1)

            raise e


def locate_and_click(
    element: ImageFile, *, tries: int = 1, clicks: int = 1,
    x_offset: int = 0, y_offset: int = 0, **kwargs
):
    """Locate an element on the screen and click it several times.

    Args:
        element (PIL.ImageFile): Image opened with PIL.
        tries (int, optional): Number of tries to find an element.
            Defaults to 1.
        clicks (int, optional): The number of times to perform click. 
            Defaults to 1.
        x_offset (int, optional): Where to move coursor further on x axis in pixels.
            To move right use x_offset > 0, to move left x_offset < 0.
            Defaults to 0.
        y_offset (int, optional): Where to move coursor further on y axis in pixels.
            To move down use y_offset > 0, to move up y_offset < 0.
            Defaults to 0.
    Returns:
        None
    """
    # TODO: check actual movements for y_offset gt 0 and lt 0.
    pyautogui.moveTo(1, 1)
    sleep(0.1)
    coords = locate_with_tries(element, tries=tries, **kwargs)
    x = coords[0] + coords[2] / 2 + x_offset
    y = coords[1] + coords[3] / 2 + y_offset
    pyautogui.moveTo(x, y)
    sleep(0.3)
    for _ in range(clicks):
        pyautogui.click()