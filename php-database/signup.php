<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Sign up</title>
	</head>
	
	<body>
		<h1>Sign up</h1>
		
		<form action="process-Sign up.php" method="post" novalidate>
		    
		    <div>
				<label for="name">Name</label>
				<input type="text" id="name" name="name"/>
			</div>

			<div>
				<label for="email">email</label>
				<input type="email" id="email" name="email"/>
			</div>
			
			<div>
				<label for="account">Account</label>
				<input type="text" id="account" name="account"/>
			</div>
			
			<div>
				<label for="password">Password</label>
				<input type="password" id="password" name="password"/>
			</div>
			
			<div>
				<label for="password_confirmation">Repeat Password</label>
				<input type="password" id="password_confirmation" name="password_confirmation"/>
			</div>

			
			<button>Sign up</button>
		</form>
	</body>
	
</html>
