# Technical Blog Styling System

This document outlines the styling system for the FastHTML Technical Blog, built on top of MonsterUI with custom enhancements.

## Architecture Overview

The styling system is composed of three main CSS files:

1. **main.css** - Core custom styles and theme enhancements
2. **utilities.css** - Utility classes for common styling patterns
3. **MonsterUI** - Base component library with theme support

## File Structure

```
fasthtml_app/static/
├── css/
│   ├── main.css          # Core custom styles
│   ├── utilities.css     # Utility classes
│   └── README.md         # This documentation
└── js/
    └── theme.js          # Theme toggle functionality
```

## MonsterUI Integration

### Theme System
- **Base Theme**: MonsterUI Blue theme (`Theme.blue`)
- **Dark/Light Mode**: Automatic theme switching with localStorage persistence
- **CSS Variables**: Uses MonsterUI's CSS custom properties for consistency

### Available MonsterUI Components
- Cards (`Card`)
- Buttons (`Button`, `ButtonT`)
- Containers (`Container`, `ContainerT`)
- Text Presets (`TextPresets`)
- Icons and links
- Form elements

## Custom Styling Guidelines

### CSS Custom Properties

We extend MonsterUI's CSS variables with our own:

```css
:root {
  /* Spacing scale */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
  --space-3xl: 4rem;
  
  /* Content constraints */
  --content-max-width: 72rem;
  --article-max-width: 48rem;
  
  /* Animation timings */
  --transition-fast: 150ms;
  --transition-normal: 250ms;
  --transition-slow: 350ms;
}
```

### Layout Classes

Use these utility classes for consistent layouts:

```html
<!-- Grid layouts -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-4">

<!-- Flex layouts -->
<div class="flex items-center justify-between">

<!-- Spacing -->
<div class="space-y-4">  <!-- Vertical spacing between children -->
<div class="space-x-2">  <!-- Horizontal spacing between children -->
```

### Typography

Leverage MonsterUI's text presets with our enhancements:

```python
# MonsterUI text presets
P("Muted text", cls=TextPresets.muted_lg)
P("Small muted text", cls=TextPresets.muted_sm)

# Custom prose styling
Div(content, cls="prose")  # For long-form content
```

### Component Styling

#### Navigation
- Uses `.main-navigation` class for flex layout
- `.nav-link` for individual navigation items
- `.nav-link.active` for current page highlighting

#### Cards
- Extends MonsterUI Card component
- `.topic-card` for topic overview cards
- `.topic-coming-soon` for disabled/upcoming topics
- `.card-featured` for highlighted content with left border

#### Code Blocks
- `.code-block-container` for code block wrapper
- `.code-title` for code block headers
- `.code-copy-btn` for copy buttons
- Integrates with HighlightJS for syntax highlighting

### Responsive Design

Mobile-first approach with breakpoints:

- **Mobile**: Base styles (< 640px)
- **sm**: 640px and up
- **md**: 768px and up  
- **lg**: 1024px and up

```css
/* Mobile first */
.grid-cols-1 { /* Mobile layout */ }

/* Tablet and up */
@media (min-width: 768px) {
  .md\:grid-cols-3 { /* Tablet layout */ }
}
```

## Theme Toggle Implementation

### JavaScript Integration
- Automatic theme detection from system preferences
- localStorage persistence for user preference
- Floating action button for manual toggle

### Usage
The theme toggle is automatically initialized when MonsterUI is ready:

```javascript
// Theme automatically applied on page load
// Button created in bottom-right corner
// Persists preference across sessions
```

## Best Practices

### MonsterUI First
1. **Use MonsterUI components first** - Check MonsterUI documentation before creating custom components
2. **Leverage CSS variables** - Use MonsterUI's color and spacing variables for consistency
3. **Extend, don't override** - Add custom styles that complement MonsterUI

### Custom Styling
1. **Follow CSS custom property naming** - Use `--space-*`, `--transition-*` patterns
2. **Use utility classes** - Prefer utilities over component-specific styles
3. **Mobile-first responsive design** - Start with mobile, enhance for larger screens

### Performance
1. **Minimize custom CSS** - Rely on MonsterUI's optimized styles
2. **Use CSS variables** - Enable dynamic theming and reduce redundancy
3. **Progressive enhancement** - Core functionality works without JavaScript

## Color System

All colors are managed through MonsterUI's CSS variables:

```css
/* Text colors */
color: var(--uk-color-emphasis);           /* High contrast text */
color: var(--uk-color-muted-foreground);   /* Secondary text */

/* Background colors */
background-color: var(--uk-color-background);      /* Page background */
background-color: var(--uk-color-muted-background); /* Secondary bg */

/* Interactive colors */
color: var(--uk-color-primary);            /* Primary brand color */
border-color: var(--uk-color-muted-border); /* Subtle borders */
```

## Interactive Elements

### Hover States
- Consistent transition timing using CSS variables
- Scale and shadow effects for cards
- Color transitions for interactive elements

### Focus States
- Keyboard navigation support with visible focus indicators
- Uses MonsterUI's focus ring system

### Loading States
- Skeleton loading animation
- Smooth transitions between states

## Accessibility

### Screen Readers
- `.sr-only` class for screen reader only content
- Proper semantic markup with MonsterUI components

### Keyboard Navigation
- Tab-accessible theme toggle
- Focus-visible styles for keyboard users

### Color Contrast
- MonsterUI ensures WCAG compliance
- Theme toggle maintains contrast in both modes

## File Loading Order

The CSS files are loaded in this order for proper cascade:

1. MonsterUI theme headers
2. HighlightJS styles  
3. KatexMarkdownJS styles
4. main.css (our core styles)
5. utilities.css (our utility classes)

This ensures MonsterUI's base styles are loaded first, then our custom enhancements can build upon them.