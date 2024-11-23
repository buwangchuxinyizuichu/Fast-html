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
	</head>
	
	<body>
		<h1>Login</h1>

        <?php if($is_invalid): ?>
            <em>Invalid Login</em>
        <?php endif; ?>

        <form method="post">
            <label for="account">account</label>
            <input type="text" name="account" id="account"
                   value="<?= htmlspecialchars($_POST["account"] ?? "") ?>">

            <label for="password">password</label>
            <input type="password" name="password" id="password">

            <button>Log in</button>
        </form>
    </body>
</html>