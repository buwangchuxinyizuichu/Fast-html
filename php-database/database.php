<?php

$servername="localhost";
$username="root";
$password="123456";
$database="login_db";

$mysqli=new mysqli($servername,$username,$password,$database);

if($mysqli->connect_errno){
    die("Connection error: ".$mysqli->connect_error);
}

return $mysqli;

?>