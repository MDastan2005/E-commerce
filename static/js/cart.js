let updateBtns = document.getElementsByClassName('update-cart')

for (const btn of updateBtns) {
	// console.log(btn.)
	btn.addEventListener("click", function() {
		let productId = this.dataset.product
		let action = this.dataset.action
		console.log("productId:", productId, "Action:", action)

		console.log("USER:", user)

		if (user == "AnonymousUser") {
			console.log("Not logged in")
		} else {
			updateUserOrder(productId, action)
		}
	})
}

const updateUserOrder = (productId, action) => {
	console.log("User is logged in, sending data..")

	let url = "/update_item/"

	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body: JSON.stringify({'productId': productId, 'action': action})
	})
	.then((response) => {
		return response.json()
	})
	.then((data) => {
		location.reload()
	})
}