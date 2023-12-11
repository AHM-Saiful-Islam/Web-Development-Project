function login() {
    // For simplicity, let's consider a successful login.
    // You would typically perform authentication on the server.

    // Redirect to the welcome page after successful login.
    window.location.href = 'welcome.html';
}

function register() {
    // You can add your registration logic here.
    // For simplicity, let's just display an alert.
    alert("Registration Successful! Click Ok to login!");

    // Assuming successful registration, redirect to the login page
    window.location.href = "login.html";
}
