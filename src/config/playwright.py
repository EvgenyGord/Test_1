import os


class PlaywrightConfig:
    PAGE_VIEWPORT_SIZE = {'width': 1920, 'height': 1080}
    ENV = os.getenv('ENV') if os.getenv('ENV') is not None else 'stage'
    BROWSER = os.getenv('BROWSER') if os.getenv('BROWSER') is not None else 'chrome'
    IS_HEADLESS = os.getenv('HEADLESS', 'False').lower() in ['true', '1']
    SLOW_MO = int(os.getenv('SLOW_MO')) if os.getenv('SLOW_MO') is not None else 50
    LOCALE = 'en-US'