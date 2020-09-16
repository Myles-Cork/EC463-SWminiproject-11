body {
  font-family: sans-serif;
}

html,
.fullscreen {
  display: flex;
  height: 100%;
  margin: 0;
  padding: 0;
  width: 100%;
}

.symptom-test {
  margin: 0 50px;
  max-width: 750px;
  display: inline-block;
}

.title {
  font-size: 3rem;
}

.navigation{
	flex: 1;
}

.navigation ul li{
	list-style: none;
	display: inline-block;
	margin: 0 20px;
}

.navigation ul li a{
	color: #000000;
	text-decoration: none;
}

#sidenav{
	width: 250px;
	height: 100vh;
	position: fixed;
	right: -250px;
	top: 0;
	background: #000000;
	z-index: 2;
	transition: 0.5s;
}

nav ul li{
	list-style: none;
	margin: 50px 20px;
}

nav ul li a{
	text-decoration: none;
	color: #fff;
}

#menuBtn{
	width: 50px;
	position: fixed;
	right: 65px;
	top: 35px;
	z-index: 2;
	cursor: pointer;
}

.btn{
	padding: 5px 12px;
	background: transparent;
	outline: none;
	border: 2px solid #000000;
	font-weight: bold;
	cursor: pointer;
	margin: 0px 12px;
}