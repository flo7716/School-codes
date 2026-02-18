<?php
// filepath: /home/florian/Documents/School-codes/SdV/cryptologie/tp_apache_https/www/testhttps/bienvenue.php

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome - Home</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        
        header {
            background: #2c3e50;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        
        nav {
            background: #34495e;
            padding: 1rem;
        }
        
        nav a {
            color: white;
            text-decoration: none;
            margin: 0 1rem;
        }
        
        nav a:hover {
            text-decoration: underline;
        }
        
        main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        
        .hero {
            background: #ecf0f1;
            padding: 3rem;
            border-radius: 5px;
            margin-bottom: 2rem;
        }
        
        .hero h2 {
            margin-bottom: 1rem;
        }
        
        .content-section {
            margin: 2rem 0;
        }
        
        footer {
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 1rem;
            margin-top: 3rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Our Website</h1>
    </header>
    
    <nav>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
    </nav>
    
    <main>
        <section class="hero">
            <h2>Hello and Welcome!</h2>
            <p>This is a classic home webpage template. Feel free to customize it with your own content.</p>
        </section>
        
        <section class="content-section" id="about">
            <h2>About Us</h2>
            <p>Learn more about what we do and our mission.</p>
        </section>
        
        <section class="content-section" id="services">
            <h2>Our Services</h2>
            <p>Discover the services we offer to our clients.</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 Your Website. All rights reserved.</p>
    </footer>
</body>
</html>