<?php

$dbhost = 'localhost';  // mysql服务器主机地址
$dbuser = 'root';            // mysql用户名
$dbpass = '123456';          // mysql用户名密码
$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
    die('连接失败: ' . mysqli_error($conn));
}
echo '连接成功<br />';

$sql = "CREATE TABLE Project_info( ".
        "id INT NOT NULL AUTO_INCREMENT, ".
        "Engineering_information VARCHAR(255) NOT NULL , ".
        "Chat_history VARCHAR(255) NOT NULL, ".
        "Project_files VARCHAR(255) NOT NULL,".
        "PRIMARY KEY ( id ))ENGINE=InnoDB DEFAULT CHARSET=utf8; ";
mysqli_select_db( $conn, 'login_db' );
$retval = mysqli_query( $conn, $sql );
if(! $retval )
{
    die('数据表创建失败: ' . mysqli_error($conn));
}
echo "数据表创建成功\n";
mysqli_close($conn);

?>