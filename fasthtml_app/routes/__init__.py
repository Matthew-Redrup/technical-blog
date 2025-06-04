"""Route modules for the FastHTML technical blog application"""

from .home import home_routes
from .rbe import rbe_routes  
from .topics import topics_routes
from .about import about_routes

__all__ = ['home_routes', 'rbe_routes', 'topics_routes', 'about_routes']