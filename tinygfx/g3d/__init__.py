# import all operation modules into the global namespace
from . import operations
from .operations import *

# pull surfaces into the namespace
from . import world_objects
from .world_objects import *

# import primitives but don't pull into namespace
from . import primitives
from .primitives import Ray, Vector, Point  # bring in basic ray properties
from . import renderers
