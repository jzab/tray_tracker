console.log("Hello World.")

$(document).onReady(){//This might be wrong, google it

	$(".example-div").click(function() {
		alert("Hey JZ!");
	})

}




//Ajax - a way to call URLS and pass information to the backend. Ajax call calls a function in views.py, call it addData(request)
//Add data adds the information from the URL Call to the database 