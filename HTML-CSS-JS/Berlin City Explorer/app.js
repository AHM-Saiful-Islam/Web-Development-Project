const bcrypt = require('bcrypt');
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

const databasePath = 'database.json';

// Registration endpoint
// Registration endpoint
app.post('/register', async (req, res) => {
    const { username, password, email } = req.body;

    // Additional logic for registration
    if (!username || !password) {
        return res.status(400).json({ message: 'Username and password are required.' });
    }

    const users = readDatabase();

    // Check if username is already taken
    if (users.some(user => user.username === username)) {
        return res.status(400).json({ message: 'Username is already taken. Please choose a different one.' });
    }

    // Hash the password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Save user to the database with hashed password
    users.push({ username, password: hashedPassword, email });
    writeDatabase(users);

    // Sending a response
    res.json({ success: true, message: 'Registration successful. You can now log in.' });
});


// Login endpoint
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    // Check if the user exists
    const existingUsers = readDatabase();
    const user = existingUsers.find(user => user.username === username);

    if (!user) {
        console.log('User not found:', username);
        return res.status(401).json({ success: false, message: 'Invalid credentials - User not found' });
    }

    // Compare the provided password with the hashed password stored in the database
    bcrypt.compare(password, user.password, (err, result) => {
        if (err || !result) {
            console.log('Incorrect password provided:', password);
            return res.status(401).json({ success: false, message: 'Invalid credentials - Incorrect password' });
        }

        res.status(200).json({ success: true, message: 'Login successful' });
    });
});

// Function to read from the database file
function readDatabase() {
    try {
        const data = fs.readFileSync(databasePath, 'utf-8');
        return JSON.parse(data);
    } catch (error) {
        console.error('Error reading database:', error);
        return [];
    }
}

// Function to write to the database file
function writeDatabase(data) {
    try {
        const jsonData = JSON.stringify(data, null, 2);
        fs.writeFileSync(databasePath, jsonData, 'utf-8');
    } catch (error) {
        console.error('Error writing to database:', error);
    }
}

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
