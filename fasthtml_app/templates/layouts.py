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
                *extra_headers,
                # Custom CSS for enhanced styling
                Style("""
                    .main-navigation {
                        display: flex;
                        gap: 1rem;
                        padding: 1rem 0;
                        border-bottom: 1px solid #e5e7eb;
                        margin-bottom: 2rem;
                    }
                    .nav-link {
                        padding: 0.5rem 1rem;
                        text-decoration: none;
                        border-radius: 0.375rem;
                        transition: background-color 0.2s;
                    }
                    .nav-link:hover {
                        background-color: #f3f4f6;
                    }
                    .nav-link.active {
                        background-color: #3b82f6;
                        color: white;
                    }
                    .topic-card {
                        border: 1px solid #e5e7eb;
                        border-radius: 0.5rem;
                        padding: 1.5rem;
                        transition: box-shadow 0.2s;
                    }
                    .topic-card:hover {
                        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                    }
                    .topic-coming-soon {
                        opacity: 0.6;
                    }
                    .code-block-container {
                        margin: 1rem 0;
                    }
                    .code-title {
                        background-color: #374151;
                        color: white;
                        padding: 0.5rem 1rem;
                        border-radius: 0.375rem 0.375rem 0 0;
                        font-size: 0.875rem;
                        font-weight: 500;
                    }
                    .math-content {
                        text-align: center;
                        margin: 1rem 0;
                    }
                    .math-inline {
                        display: inline;
                    }
                """)
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
    return Titled(f"Error {error_code} - Matthew Redrup's Technical Blog",
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