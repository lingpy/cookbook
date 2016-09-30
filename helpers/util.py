from pathlib import Path
import os
from functools import partial
def helper_path(*comps):
    return os.path.join(os.path.dirname(__file__), *comps)
data_path = partial(helper_path, 'data')
