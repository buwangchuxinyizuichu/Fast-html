<?php

session_start();

if(isset($_SESSION["user_id"])){
    $mysqli = require __DIR__ . "/database.php";
    $sql = "SELECT * FROM user1
            WHERE id = {$_SESSION["user_id"]}";
    $result = $mysqli->query($sql);
    $user = $result->fetch_assoc();
}
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Home</title>
	</head>
	
	<body>
		<h1>Home</h1>

        <?php if(isset($user)): ?>
            <p>Hello <?= htmlspecialchars($user["name"]) ?></p>
            <p><a href="logout.php">Log out</a></p>
        <?php else: ?>
            <p><a href="login.php">Log in</a> or <a href="signup.php">sign up</a></p>
        <?php endif; ?>

    </body>
</html>