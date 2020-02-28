import pytest
import logging

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope='session', autouse=True)
def pikcha():
    yield
    LOGGER.info(r'''           
           \       /
             .---. 
        '-.  |   |  .-'
          ___|   |___
     -=  [           ]  =-
         `---.   .---' 
      __||__ |   | __||__
      '-..-' |   | '-..-'
        ||   |   |   ||
        ||_.-|   |-,_||
      .-"`   `"`'`   `"-.
    .'                   '.''')
