function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Example: Send a POST request to the server
    fetch('http://localhost:3000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the response message
        document.getElementById("loginMessage").innerHTML = data.message;

        // Log the response for debugging
        console.log('Login Response:', data);

        // Redirect to welcome page after successful login
        if (data.success) {
            console.log('Redirecting to welcome.html');
            window.location.href = 'welcome.html'; // Redirect after successful login
        } else {
            throw new Error('Login unsuccessful');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("loginMessage").innerHTML = 'An error occurred.';
    });
}
