"""Layout templates for the FastHTML blog application"""

from fasthtml.common import *
from monsterui.all import *
from technical_blog.blog_components import create_navigation

def base_layout(title: str = "Matthew Redrup's Technical Blog", 
                current_section: str = None,
                extra_headers: tuple = ()):
    """
    Base layout template with common structure
    
    Args:
        title: Page title
        current_section: Current navigation section for highlighting
        extra_headers: Additional headers to include
    """
    def layout_wrapper(content):
        return Html(
            Head(
                Meta(charset="utf-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1"),
                Meta(name="description", content="Technical blog exploring AI, cybersecurity, and software engineering"),
                Meta(name="author", content="Matthew Redrup"),
                Title(title),
                *Theme.blue.headers(),
                HighlightJS(),
                KatexMarkdownJS(),
                Link(rel="stylesheet", href="/static/css/main.css"),
                Link(rel="stylesheet", href="/static/css/utilities.css"),
                *extra_headers
            ),
            Body(
                Div(
                    create_navigation(current_section),
                    content,
                    cls="min-h-screen bg-gray-50",
                    id="app"
                )
            )
        )
    return layout_wrapper

def blog_layout(title: str, current_section: str = None):
    """
    Layout specifically for blog content pages
    
    Args:
        title: Page title
        current_section: Current navigation section
    """
    def layout_wrapper(content):
        return base_layout(title, current_section)(
            Container(
                content,
                cls=ContainerT.xl
            )
        )
    return layout_wrapper

def error_layout(error_code: int, error_message: str):
    """
    Layout for error pages
    
    Args:
        error_code: HTTP error code (404, 500, etc.)
        error_message: Error description
    """
    return (
        Title(f"Error {error_code} - Matthew Redrup's Technical Blog"),
        create_navigation(None),
        Container(
            Card(
                Div(
                    H1(f"Error {error_code}", cls="text-6xl font-bold text-gray-600 mb-4"),
                    H2(error_message, cls="text-2xl font-semibold mb-6"),
                    P("Sorry, something went wrong. Here are some things you can try:", cls="mb-4"),
                    Ul(
                        Li(A("Go back to the homepage", href="/", cls="text-blue-600 hover:underline")),
                        Li(A("Browse all topics", href="/topics/", cls="text-blue-600 hover:underline")),
                        Li(A("View the RBE series", href="/rbe/", cls="text-blue-600 hover:underline")),
                        Li(A("Check out the components demo", href="/demo/", cls="text-blue-600 hover:underline")),
                        cls="space-y-2 mb-6"
                    ),
                    Button("← Back to Home", 
                          onclick="window.location.href='/'",
                          cls=ButtonT.primary,
                          submit=False),
                    cls="text-center py-12"
                ),
                cls="p-8"
            ),
            cls=ContainerT.xl
        )
    )