"""
FastHTML Technical Blog Application

Main application entry point for the interactive technical blog.
"""

from fasthtml.common import *
from monsterui.all import *
from pathlib import Path
from technical_blog.blog_components import create_navigation, topic_card, math_block, code_block

# Initialize FastHTML app with MonsterUI theme and JS libraries
app, rt = fast_app(
    hdrs=(
        *Theme.blue.headers(),
        HighlightJS(),  # Syntax highlighting for code blocks
        KatexMarkdownJS()  # Math rendering for LaTeX expressions
    ),
    static_path="static"
)

# Static file serving
@rt("/static/{path:path}")
def serve_static(path: str):
    return FileResponse(f"static/{path}")

@rt("/")
def home():
    """Homepage of the technical blog"""
    socials = (
        ('github', 'https://github.com/your-username'),
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
                    cls=f"{TextPresets.muted_lg} mb-4"
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

@rt("/rbe/")
def rbe_index():
    """RBE series index page"""
    return Titled("Recursive Bayesian Estimators in Cybersecurity",
        create_navigation("RBE"),
        Container(
            Card(
                H2("RBE Series Overview", cls="text-2xl font-semibold mb-4"),
                P("A comprehensive series on RBE theory and implementation.", cls="mb-4"),
                Divider(),
                P("Content will be loaded from nbs/rbe/index.ipynb", 
                  cls=TextPresets.muted),
                Button("← Back to Home", 
                      onclick="window.location.href='/'",
                      cls=ButtonT.secondary,
                      submit=False),
                cls="p-6"
            ),
            cls=ContainerT.xl
        )
    )

@rt("/demo/")
def components_demo():
    """Demo page showing all blog components"""
    sample_code = """def recursive_bayesian_update(prior, likelihood, evidence):
    \"\"\"Update belief using Bayes' theorem\"\"\"
    posterior = (likelihood * prior) / evidence
    return posterior

# Example usage
prior_belief = 0.3
likelihood = 0.8
evidence = 0.6
updated_belief = recursive_bayesian_update(prior_belief, likelihood, evidence)
print(f"Updated belief: {updated_belief:.3f}")"""

    sample_math = r"P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}"
    
    return Titled("Blog Components Demo",
        create_navigation("Demo"),
        Container(
            Card(
                H1("Blog Components Demo", cls="text-3xl font-bold mb-6"),
                
                H2("Navigation Component", cls="text-2xl font-semibold mb-4"),
                P("The navigation bar above is generated using the create_navigation() component.", cls="mb-6"),
                
                H2("Code Block Component", cls="text-2xl font-semibold mb-4"),
                P("Syntax-highlighted code with copy functionality:", cls="mb-4"),
                code_block(sample_code, "python", "Recursive Bayesian Update"),
                
                H2("Math Block Component", cls="text-2xl font-semibold mb-4 mt-8"),
                P("LaTeX math rendering with KaTeX:", cls="mb-4"),
                math_block(sample_math, block=True),
                P("And here's inline math: ", cls="mt-4"),
                math_block(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", block=False),
                
                H2("Topic Cards Component", cls="text-2xl font-semibold mb-4 mt-8"),
                P("Cards for displaying topics:", cls="mb-4"),
                Div(
                    topic_card(
                        "Recursive Bayesian Estimators", 
                        "Learn the mathematical foundations and practical applications", 
                        "/rbe/", 
                        "available"
                    ),
                    topic_card(
                        "Advanced Neural Networks", 
                        "Deep dive into transformer architectures and attention mechanisms", 
                        "/neural/", 
                        "coming soon"
                    ),
                    cls="grid grid-cols-1 md:grid-cols-2 gap-4"
                ),
                
                cls="p-8"
            ),
            cls=ContainerT.xl
        )
    )


serve()