<?php

$is_invalid=false;

if($_SERVER["REQUEST_METHOD"] === "POST"){
    $mysqli = require __DIR__ . "/database.php";
    $sql = sprintf("SELECT * FROM user1
                    WHERE account ='%s'",
                    $mysqli->real_escape_string($_POST["account"]));

    $result = $mysqli->query($sql);
    $user = $result->fetch_assoc();

    if($user)
    {
         if(password_verify($_POST["password"],$user["password"])){
            
            session_start();
            
            session_regenerate_id();

            $_SESSION["user_id"]=$user["id"];
            
            header("Location: index.php");
            exit;        
        }

    }

    $is_invalid=true;
}

?>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Login</title>
		<link rel="stylesheet" href="css/login.css" />
		<style>
		    body {
		        display: flex;
		        justify-content: center;
		        align-items: center;
		        height: 100vh;
		        margin: 0;
		    }
		   .form {
		        width: 100%;
		        max-width: 400px;
		        padding: 20px;
		        border: 1px solid #ccc;
		        border-radius: 5px;
		    }
		</style>
	</head>
	
	<body>


        <form method="post" class="form">
			<p class="title">Sign up </p >
			<p class="message">Signup now and get full access to our web. </p >
            <?php if($is_invalid): ?>
            <em>Invalid Login</em>
        <?php endif; ?>
  <label for="account">
            <input class="input" type="text" placeholder="" required="" id="account" name="account"
			 value="<?= htmlspecialchars($_POST["account"] ?? "")?>">
            <span>Account</span>
        </label>
            <label for="password">
                <input class="input" type="password" placeholder="" required="" name="password" id="password"> 
                <span>Password</span>
            </label>

            <button class="submit">Submit</button>
            <p class="signin">Don't have an account yet? Register now 