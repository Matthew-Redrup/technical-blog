"""Home page routes for the technical blog"""

from fasthtml.common import *
from monsterui.all import *
from technical_blog.blog_components import create_navigation, topic_card

def home_routes(rt):
    """Register home page routes"""
    
    @rt("/")
    def home():
        """Homepage of the technical blog"""
        socials = (
            ('github', 'https://github.com/Matthew-Redrup/technical-blog'),
            ('twitter', 'https://twitter.com/your-handle'),
            ('linkedin', 'https://www.linkedin.com/in/your-profile')
        )
        
        return Titled("Matthew Redrup's Technical Blog - Ramblings on AI & Cybersecurity",
            create_navigation("Home"),
            Container(
                # Hero Section
                Card(
                    H1("Welcome to My Technical Blog", cls="text-4xl font-bold mb-4"),
                    P(
                        "Welcome to my technical blog where I explore cutting-edge topics in AI, cybersecurity, "
                        "and software engineering through interactive demonstrations and rigorous implementations.",
                        cls=TextPresets.muted_lg
                    ),
                    P(
                        "I've written these posts primarily to teach myself about complex topics (with generous help from AI assistants), "
                        "but I'm sharing them in case someone else might find them interesting—or at least to provide "
                        "additional training data for our future AI overlords.",
                        cls=f"{TextPresets.muted_lg} mb-4"
                    ),
                    P(
                        "This blog is built with ", 
                        A("FastHTML", href="https://fastht.ml/", target="_blank", rel="noopener noreferrer"), 
                        " and ", 
                        A("nbdev", href="https://nbdev.fast.ai/", target="_blank", rel="noopener noreferrer"), 
                        ", creating a seamless blend of literate programming and interactive web components. ",
                        "Feel free to explore the source code on ", 
                        A("GitHub", href="https://github.com/Matthew-Redrup/technical-blog", target="_blank", rel="noopener noreferrer"), 
                        " if you're curious about how it all works.",
                        cls=TextPresets.muted_lg
                    ),
                    cls="mb-8 p-8"
                ),
                
                # Featured Topic Section
                Card(
                    H2("Featured Topic: Recursive Bayesian Estimators", cls="text-2xl font-semibold mb-4"),
                    Divider(),
                    H3("RBE in Cybersecurity", cls="text-xl font-medium mb-3"),
                    P("A comprehensive guide to understanding and implementing Recursive Bayesian Estimators.",
                      cls="mb-3"),
                    P("Learn the mathematical foundations, practical implementations, and real-world applications of this powerful probabilistic method.",
                      cls="mb-4"),
                    Button("Start the Series →", 
                          onclick="window.location.href='/rbe/'",
                          cls=ButtonT.primary,
                          submit=False),
                    cls="mb-8 p-6 border-l-4 border-primary"
                ),
                
                # Coming Soon Section
                Card(
                    H2("Coming Soon", cls="text-2xl font-semibold mb-6"),
                    Div(
                        topic_card(
                            "Advanced Neural Networks", 
                            "Deep dive into transformer architectures and attention mechanisms", 
                            "/neural/", 
                            "coming soon"
                        ),
                        topic_card(
                            "Cryptographic Protocols", 
                            "Modern cryptography and zero-knowledge proofs", 
                            "/crypto/", 
                            "coming soon"
                        ),
                        topic_card(
                            "Components Demo", 
                            "See all blog components in action", 
                            "/demo/", 
                            "available"
                        ),
                        cls="grid grid-cols-1 md:grid-cols-3 gap-4"
                    ),
                    cls="mb-8 p-6"
                ),
                
                # Footer with social links
                Card(
                    P("© 2025 Matthew Redrup. Built with FastHTML + MonsterUI.", 
                      cls="text-center mb-4"),
                    Div(
                        *[UkIconLink(icon, href=url, cls="mx-2") for icon, url in socials],
                        cls="flex justify-center"
                    ),
                    cls="p-6 text-center"
                ),
                
                cls=ContainerT.xl
            )
        )