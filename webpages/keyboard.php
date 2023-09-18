<?php
// your_php_script.php

if ($_SERVER["REQUEST_METHOD"] === "POST") {
  $name = $_POST["name"];

    // Process the data (e.g., save to a database, send an email)

    // Return a response (e.g., a success message)
  $servername = "localhost"; // Replace with your database server address
$username = "root"; // Replace with your database username
$password = ""; // Replace with your database password
$dbname = "wifi"; // Replace with your database name

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$sql = "INSERT INTO wifi (cmd) VALUES ('$name')";
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}


}

?>
