"""RBE (Recursive Bayesian Estimators) routes"""

from fasthtml.common import *
from monsterui.all import *
from technical_blog.blog_components import create_nav

def rbe_routes(rt):
    """Register RBE series routes"""
    
    @rt("/rbe/")
    def rbe_index():
        """RBE series index page"""
        return (
            Title("Recursive Bayesian Estimators in Cybersecurity"),
            create_nav("RBE"),
            Container(
                Card(
                    H1("Recursive Bayesian Estimators", cls="text-3xl font-bold mb-6"),
                    H2("A Comprehensive Guide to RBE Theory and Implementation", cls="text-xl font-medium mb-4"),
                    
                    P("This series provides a deep dive into Recursive Bayesian Estimators (RBE), "
                      "covering everything from mathematical foundations to practical cybersecurity applications.",
                      cls="mb-6"),
                    
                    Divider(),
                    
                    H3("Series Overview", cls="text-lg font-semibold mb-4"),
                    
                    Card(
                        H4("Part 1: Mathematical Foundations", cls="font-semibold mb-2"),
                        P("Introduction to Bayesian inference, probability theory, and the recursive framework.", cls="mb-3"),
                        A("Read Part 1 →", href="/rbe/foundations/", cls="text-blue-600 hover:underline"),
                        cls="p-4 mb-4 bg-slate-50"
                    ),
                    
                    Card(
                        H4("Part 2: Implementation Strategies", cls="font-semibold mb-2"),
                        P("Practical Python implementations with performance optimizations.", cls="mb-3"),
                        A("Read Part 2 →", href="/rbe/implementation/", cls="text-blue-600 hover:underline"),
                        cls="p-4 mb-4 bg-slate-50"
                    ),
                    
                    Card(
                        H4("Part 3: Cybersecurity Applications", cls="font-semibold mb-2"),
                        P("Real-world applications in network anomaly detection and threat assessment.", cls="mb-3"),
                        A("Read Part 3 →", href="/rbe/cybersecurity/", cls="text-blue-600 hover:underline"),
                        cls="p-4 mb-4 bg-slate-50"
                    ),
                    
                    Div(
                        Button("← Back to Home", 
                              onclick="window.location.href='/'",
                              cls=ButtonT.secondary,
                              submit=False),
                        cls="mt-6"
                    ),
                    
                    cls="p-8"
                ),
                cls=ContainerT.xl
            )
        )
    
    @rt("/rbe/foundations/")
    def rbe_foundations():
        """RBE mathematical foundations"""
        return (
            Title("RBE: Mathematical Foundations"),
            create_nav("RBE"),
            Container(
                Card(
                    H1("Mathematical Foundations of RBE", cls="text-3xl font-bold mb-6"),
                    P("Content will be loaded from nbs/rbe/ notebooks when available.", 
                      cls=TextPresets.muted_sm),
                    Button("← Back to RBE Series", 
                          onclick="window.location.href='/rbe/'",
                          cls=ButtonT.secondary,
                          submit=False),
                    cls="p-8"
                ),
                cls=ContainerT.xl
            )
        )
    
    @rt("/rbe/implementation/")
    def rbe_implementation():
        """RBE implementation strategies"""
        return (
            Title("RBE: Implementation Strategies"),
            create_nav("RBE"),
            Container(
                Card(
                    H1("Implementation Strategies", cls="text-3xl font-bold mb-6"),
                    P("Content will be loaded from nbs/rbe/ notebooks when available.", 
                      cls=TextPresets.muted_sm),
                    Button("← Back to RBE Series", 
                          onclick="window.location.href='/rbe/'",
                          cls=ButtonT.secondary,
                          submit=False),
                    cls="p-8"
                ),
                cls=ContainerT.xl
            )
        )
    
    @rt("/rbe/cybersecurity/")
    def rbe_cybersecurity():
        """RBE cybersecurity applications"""
        return (
            Title("RBE: Cybersecurity Applications"),
            create_nav("RBE"),
            Container(
                Card(
                    H1("Cybersecurity Applications", cls="text-3xl font-bold mb-6"),
                    P("Content will be loaded from nbs/rbe/ notebooks when available.", 
                      cls=TextPresets.muted_sm),
                    Button("← Back to RBE Series", 
                          onclick="window.location.href='/rbe/'",
                          cls=ButtonT.secondary,
                          submit=False),
                    cls="p-8"
                ),
                cls=ContainerT.xl
            )
        )