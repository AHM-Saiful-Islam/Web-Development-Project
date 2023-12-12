function register() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const email = document.getElementById("email").value;

    // Example: Send a POST request to the server
    fetch('http://localhost:3000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password, email }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the response message
        document.getElementById("registerMessage").innerHTML = data.message;

        // Redirect to login page after successful registration
        if (data.success) {
            setTimeout(() => {
                window.location.href = 'login.html';
            }, 2000); // Redirect after 2 seconds (adjust as needed)
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("registerMessage").innerHTML = 'An error occurred.';
    });
}
