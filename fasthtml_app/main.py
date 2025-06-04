"""
FastHTML Technical Blog Application

Main application entry point for the interactive technical blog.
Follows FastHTML and nbdev best practices with modular routing.
"""

from fasthtml.common import *
from monsterui.all import *
from pathlib import Path
import os

# Import route modules
from routes import home_routes, rbe_routes, topics_routes, about_routes
from templates import error_layout

# Initialize FastHTML app with MonsterUI theme and JS libraries
app, rt = fast_app(
    hdrs=(
        *Theme.blue.headers(),
        HighlightJS(),  # Syntax highlighting for code blocks
        KatexMarkdownJS()  # Math rendering for LaTeX expressions
    ),
    static_path="static"
)

# Enhanced static file serving with proper MIME types
@rt("/static/{path:path}")
def serve_static(path: str):
    """Serve static files with proper MIME type detection"""
    static_path = Path("static") / path
    if static_path.exists() and static_path.is_file():
        return FileResponse(static_path)
    else:
        return error_layout(404, "Static file not found")

# Register all route modules
home_routes(rt)
rbe_routes(rt)
topics_routes(rt)
about_routes(rt)

# Error handling routes
@rt("/404")
def not_found():
    """404 Not Found page"""
    return error_layout(404, "Page Not Found")

@rt("/500")  
def server_error():
    """500 Internal Server Error page"""
    return error_layout(500, "Internal Server Error")

# Health check endpoint for monitoring
@rt("/health")
def health_check():
    """Simple health check endpoint"""
    return {"status": "healthy", "service": "technical-blog"}

# 404 catch-all route - must be last
@rt("/{path:path}")
def catch_all(path: str):
    """Catch all undefined routes and return 404"""
    if path not in ["favicon.ico"]:  # Ignore common browser requests
        return error_layout(404, f"The page '/{path}' was not found")

def main():
    """Main entry point for development server"""
    port = int(os.getenv("PORT", 5001))
    host = os.getenv("HOST", "127.0.0.1")
    
    print(f"🚀 Starting FastHTML Technical Blog on {host}:{port}")
    print(f"🌐 Open: http://localhost:{port}")
    
    serve(host=host, port=port)

if __name__ == "__main__":
    main()