"""Future topics and general topic routes"""

from fasthtml.common import *
from monsterui.all import *
from technical_blog.blog_components import create_navigation, topic_card, math_block, code_block

def topics_routes(rt):
    """Register topic-related routes"""
    
    @rt("/topics/")
    def topics_index():
        """Future topics overview page"""
        return (
            Title("Future Topics - Matthew Redrup's Technical Blog"),
            create_navigation("Future Topics"),
            Container(
                Card(
                    H1("Future Topics", cls="text-3xl font-bold mb-6"),
                    P("Upcoming topics I plan to explore in depth on this blog.", cls="mb-6"),
                    
                    Div(
                        topic_card(
                            "Advanced Neural Networks", 
                            "Deep dive into transformer architectures, attention mechanisms, and modern deep learning techniques", 
                            "/neural/", 
                            "coming soon"
                        ),
                        topic_card(
                            "Cryptographic Protocols", 
                            "Modern cryptography, zero-knowledge proofs, and blockchain security", 
                            "/crypto/", 
                            "coming soon"
                        ),
                        topic_card(
                            "Distributed Systems", 
                            "Consensus algorithms, fault tolerance, and scalable architecture patterns", 
                            "/distributed/", 
                            "coming soon"
                        ),
                        topic_card(
                            "Quantum Computing", 
                            "Quantum algorithms, error correction, and near-term quantum applications", 
                            "/quantum/", 
                            "coming soon"
                        ),
                        topic_card(
                            "Adversarial AI", 
                            "Attack vectors, defensive strategies, and AI safety considerations", 
                            "/adversarial/", 
                            "coming soon"
                        ),
                        topic_card(
                            "Network Security", 
                            "Protocol analysis, intrusion detection, and network forensics", 
                            "/network-security/", 
                            "coming soon"
                        ),
                        cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
                    ),
                    
                    Button("← Back to Home", 
                          onclick="window.location.href='/'",
                          cls=f"{ButtonT.secondary} mt-8",
                          submit=False),
                    
                    cls="p-8"
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

        sample_math = r"P(H|E) = \\frac{P(E|H) \\cdot P(H)}{P(E)}"
        
        return (
            Title("Blog Components Demo"),
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
                    math_block(r"x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}", block=False),
                    
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
                    
                    Button("← Back to Home", 
                          onclick="window.location.href='/'",
                          cls=f"{ButtonT.secondary} mt-8",
                          submit=False),
                    
                    cls="p-8"
                ),
                cls=ContainerT.xl
            )
        )