<?php
// filepath: /home/florian/Documents/School-codes/SdV/cryptologie/tp_apache_https/www/testhttps/login.php

session_start();

$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = isset($_POST['username']) ? htmlspecialchars($_POST['username'], ENT_QUOTES, 'UTF-8') : '';
    $password = isset($_POST['password']) ? $_POST['password'] : '';
    
    // Simple validation
    if (empty($username) || empty($password)) {
        $error = 'Username and password are required.';
    } elseif (strlen($password) < 6) {
        $error = 'Password must be at least 6 characters long.';
    } else {
        // Basic authentication (replace with database check in production)
        if ($username === 'admin' && $password === 'password123') {
            $_SESSION['user'] = $username;
            header('Location: accueil.html');
            exit;
        } else {
            $error = 'Invalid username or password.';
        }
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
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
            background: #ecf0f1;
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
            text-align: center;
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
            max-width: 400px;
            margin: 3rem auto;
            padding: 2rem;
            background: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .login-form h2 {
            margin-bottom: 1.5rem;
            text-align: center;
        }
        
        .form-group {
            margin-bottom: 1rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        
        input {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #bdc3c7;
            border-radius: 4px;
            font-size: 1rem;
        }
        
        input:focus {
            outline: none;
            border-color: #2c3e50;
            box-shadow: 0 0 5px rgba(44,62,80,0.3);
        }
        
        button {
            width: 100%;
            padding: 0.75rem;
            background: #2c3e50;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
        }
        
        button:hover {
            background: #34495e;
        }
        
        .error {
            color: #e74c3c;
            margin-bottom: 1rem;
            padding: 0.75rem;
            background: #fadbd8;
            border-radius: 4px;
            text-align: center;
        }
        
        .back-link {
            text-align: center;
            margin-top: 1rem;
        }
        
        .back-link a {
            color: #2c3e50;
            text-decoration: none;
        }
        
        .back-link a:hover {
            text-decoration: underline;
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
        <h1>Login</h1>
    </header>
    
    <nav>
        <a href="accueil.html">Home</a>
        <a href="bienvenue.php">Welcome</a>
    </nav>
    
    <main>
        <section class="login-form">
            <h2>Sign In</h2>
            
            <?php if (!empty($error)): ?>
                <div class="error"><?php echo $error; ?></div>
            <?php endif; ?>
            
            <form method="POST" action="">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" name="username" required>
                </div>
                
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" required>
                </div>
                
                <button type="submit">Login</button>
            </form>
            
            <div class="back-link">
                <a href="accueil.html">Back to Home</a>
            </div>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 Your Website. All rights reserved.</p>
    </footer>
</body>
</html>