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


document.getElementById('openaiButton').addEventListener('click', async () => {
    const query = document.getElementById('userQuery').value; // Get user input
    const outputElement = document.getElementById('openaiOutput');

    console.log('User input query:', query); // Debugging: Log user input

    try {
        // Send POST request to Flask endpoint
        const response = await fetch('http://127.0.0.1:5000/make_decision', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_query: query })
        });

        // Log the entire response object
        console.log('Response object:', response);

        if (!response.ok) {
            console.error('Response error:', response.status, response.statusText);
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json(); // Parse JSON response
        console.log('Parsed response data:', data); // Debugging: Log parsed response
        outputElement.textContent = data['GPT Response'] || data['error']; // Display GPT response or error
    } catch (error) {
        console.error('Error in fetch request:', error); // Debugging: Log errors
        outputElement.textContent = 'An error occurred. Please try again.';
    }
});


document.addEventListener("DOMContentLoaded", () => {
    const graphImg = document.getElementById("graph");
    // Flask server URL hosting the plot
    const flaskServerURL = "http://127.0.0.1:5000/plot";

    // Set the image source to Flask endpoint
    graphImg.src = flaskServerURL;
});