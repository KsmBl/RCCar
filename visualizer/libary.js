function loadTopbar(parent)
{
	var xhr = new XMLHttpRequest();
	xhr.open('GET', '/data/html/topbar.html', true);
	xhr.onreadystatechange = function() {
		if (xhr.readyState == 4 && xhr.status == 200) {
			parent.innerHTML = xhr.responseText;
		}
	};
	xhr.send();
}

async function postData(url = "", data = {})
{
	const response = await fetch(`https://mcservermieten.de/api/${url}`, {
		method: "POST",
		mode: "cors",
		cache: "no-cache",
		credentials: "same-origin",
		headers: {
			"Content-Type": "application/json",
		},
		redirect: "follow",
		referrerPolicy: "no-referrer",
		body: JSON.stringify(data),
	});
	return response.json();
}

async function getJson(url = "")
{
	const response = await fetch(`https://mcservermieten.de/api/${url}`);
	const _response = await response.json();
	return _response;
}
