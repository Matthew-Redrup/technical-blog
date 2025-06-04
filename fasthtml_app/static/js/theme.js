/**
 * Theme Toggle Functionality
 * Manages dark/light theme switching with localStorage persistence
 */

(function() {
    'use strict';
    
    // Theme constants
    const THEME_KEY = 'technical-blog-theme';
    const THEME_DARK = 'dark';
    const THEME_LIGHT = 'light';
    
    // Check if MonsterUI theme functions are available
    function hasMonsterUITheme() {
        return typeof window.setDarkMode !== 'undefined' && 
               typeof window.setLightMode !== 'undefined';
    }
    
    // Get current theme from localStorage or system preference
    function getCurrentTheme() {
        const stored = localStorage.getItem(THEME_KEY);
        if (stored) return stored;
        
        // Check system preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return THEME_DARK;
        }
        return THEME_LIGHT;
    }
    
    // Apply theme
    function applyTheme(theme) {
        if (!hasMonsterUITheme()) {
            console.warn('MonsterUI theme functions not available');
            return;
        }
        
        if (theme === THEME_DARK) {
            window.setDarkMode();
        } else {
            window.setLightMode();
        }
        
        // Update theme toggle button icon
        updateThemeToggleIcon(theme);
        
        // Store preference
        localStorage.setItem(THEME_KEY, theme);
    }
    
    // Update theme toggle button icon
    function updateThemeToggleIcon(theme) {
        const toggle = document.querySelector('.theme-toggle');
        if (!toggle) return;
        
        const iconHtml = theme === THEME_DARK 
            ? '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>'
            : '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" /></svg>';
        
        toggle.innerHTML = iconHtml;
    }
    
    // Toggle theme
    function toggleTheme() {
        const current = getCurrentTheme();
        const next = current === THEME_DARK ? THEME_LIGHT : THEME_DARK;
        applyTheme(next);
    }
    
    // Create theme toggle button
    function createThemeToggle() {
        const button = document.createElement('button');
        button.className = 'theme-toggle';
        button.setAttribute('aria-label', 'Toggle theme');
        button.addEventListener('click', toggleTheme);
        document.body.appendChild(button);
    }
    
    // Initialize theme on page load
    function initializeTheme() {
        // Wait for MonsterUI to be ready
        const checkInterval = setInterval(() => {
            if (hasMonsterUITheme()) {
                clearInterval(checkInterval);
                
                // Apply saved theme
                const theme = getCurrentTheme();
                applyTheme(theme);
                
                // Create toggle button
                createThemeToggle();
                
                // Listen for system theme changes
                if (window.matchMedia) {
                    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
                        if (!localStorage.getItem(THEME_KEY)) {
                            applyTheme(e.matches ? THEME_DARK : THEME_LIGHT);
                        }
                    });
                }
            }
        }, 100);
        
        // Timeout after 5 seconds
        setTimeout(() => clearInterval(checkInterval), 5000);
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeTheme);
    } else {
        initializeTheme();
    }
})();