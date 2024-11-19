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


document.getElementById("randomButton").onclick = function() { generateNumber() };

function generateNumber() {
const url = 'http://127.0.0.1:5000/compute';
fetch(url)
    .then(response => response.json()) // Convert the response to JSON
    .then(data => {
        // Display the generated number
        document.getElementById("generatedOutput").innerHTML = JSON.stringify(data.generatedNumber);
    })
    .catch(error => console.error('Error:', error)); // Handle any errors
}


document.getElementById("openaiButton").onclick = function() { generateText() };

function generateText() {
const url = 'http://127.0.0.1:5000/genai';
fetch(url)
    .then(response => response.json()) // Convert the response to JSON
    .then(data => {
        // Display the generated number
        document.getElementById("openaiOutput").innerHTML = JSON.stringify(data['GPT Response']);
    })
    .catch(error => console.error('Error:', error)); // Handle any errors
}

