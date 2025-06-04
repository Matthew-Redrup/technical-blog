"""About page routes"""

from fasthtml.common import *
from monsterui.all import *
from technical_blog.blog_components import create_navigation

def about_routes(rt):
    """Register about page routes"""
    
    @rt("/about/")
    def about():
        """About page"""
        return (
            Title("About - Matthew Redrup's Technical Blog"),
            create_navigation("About"),
            Container(
                Card(
                    H1("About This Blog", cls="text-3xl font-bold mb-6"),
                    
                    Card(
                        H2("The Author", cls="text-2xl font-semibold mb-4"),
                        P("Hi, I'm Matthew Redrup. I'm passionate about AI, cybersecurity, and software engineering. "
                          "This blog serves as my learning laboratory where I explore complex technical topics "
                          "through hands-on implementation and rigorous analysis.", cls="mb-4"),
                        P("While I write these posts primarily to teach myself, I'm sharing them in case they "
                          "might be useful to others—or at least provide some interesting training data for "
                          "our future AI overlords.", cls="mb-4"),
                        cls="p-6 mb-6 bg-slate-50"
                    ),
                    
                    Card(
                        H2("Technology Stack", cls="text-2xl font-semibold mb-4"),
                        P("This blog is built using modern Python web technologies:", cls="mb-4"),
                        Ul(
                            Li(Strong("FastHTML"), ": A modern Python web framework for building interactive applications"),
                            Li(Strong("nbdev"), ": Literate programming with Jupyter notebooks"),
                            Li(Strong("MonsterUI"), ": Professional UI component library"),
                            Li(Strong("GitHub Pages"), ": Automatic documentation hosting"),
                            cls="space-y-2 mb-4"
                        ),
                        P("The combination creates a seamless workflow from exploratory research in notebooks "
                          "to production-ready interactive web components.", cls="mb-4"),
                        cls="p-6 mb-6 bg-slate-50"
                    ),
                    
                    Card(
                        H2("Philosophy", cls="text-2xl font-semibold mb-4"),
                        P("I believe in:", cls="mb-4"),
                        Ul(
                            Li(Strong("Learning in public"), ": Sharing the journey, not just the destination"),
                            Li(Strong("Rigor with accessibility"), ": Mathematical precision explained clearly"),
                            Li(Strong("Interactive exploration"), ": Hands-on components that let you experiment"),
                            Li(Strong("Open source"), ": All code available for learning and adaptation"),
                            Li(Strong("AI-assisted learning"), ": Embracing AI tools while maintaining understanding"),
                            cls="space-y-2 mb-4"
                        ),
                        cls="p-6 mb-6 bg-slate-50"
                    ),
                    
                    Card(
                        H2("Get in Touch", cls="text-2xl font-semibold mb-4"),
                        P("Feel free to reach out if you have questions, suggestions, or just want to discuss "
                          "any of the topics covered here:", cls="mb-4"),
                        Div(
                            A("GitHub", href="https://github.com/Matthew-Redrup/technical-blog", 
                              target="_blank", rel="noopener noreferrer", cls="mr-4 text-blue-600 hover:underline"),
                            A("LinkedIn", href="https://www.linkedin.com/in/your-profile", 
                              target="_blank", rel="noopener noreferrer", cls="mr-4 text-blue-600 hover:underline"),
                            A("Twitter", href="https://twitter.com/your-handle", 
                              target="_blank", rel="noopener noreferrer", cls="text-blue-600 hover:underline"),
                            cls="mb-4"
                        ),
                        cls="p-6 mb-6 bg-slate-50"
                    ),
                    
                    Button("← Back to Home", 
                          onclick="window.location.href='/'",
                          cls=ButtonT.secondary,
                          submit=False),
                    
                    cls="p-8"
                ),
                cls=ContainerT.xl
            )
        )