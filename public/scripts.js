// This is a placeholder file for any JavaScript functionality you'd like to add in the future.
// You can add things like smooth scrolling, dynamic content loading, etc.

// Example: Smooth scrolling to sections
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
