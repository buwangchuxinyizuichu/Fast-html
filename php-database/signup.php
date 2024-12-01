<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Sign up</title>
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
		<link rel="stylesheet" href="css/signup.css" />
	</head>
	
	<body>		
	<form class="form" action="process-Sign up.php" method="post" novalidate>
		    <p class="title">Sign upr </p >
		    <p class="message">Signup now and get full access to our web. </p >
		    
				<label for="name">
				        <input class="input" type="name" id="name" name="name" placeholder="" required="">
				        <span>Name</span>
				</label> 
			<label for="email">
			        <input class="input" type="email" id="email" name="email" placeholder="" required="">
			        <span>Email</span>
			</label>
			
			<label for="account">
			        <input class="input" type="account" id="account" name="account" placeholder="" required="">
			        <span>Account</span>
			</label>
			
			<label for="password">
			        <input class="input" type="password" id="password" name="password" placeholder="" required="">
			        <span>Password</span>
			</label>
			
			<label for="password">
			        <input class="input" type="password" id="password_confirmation" name="password_confirmation" placeholder="" required="">
			        <span>Password</span>
			</label>
			
			<button class="submit">Submit</button>
			<p class="signin">Already have an acount ? Signin </p >
		</form>
	</body>
	
</html>