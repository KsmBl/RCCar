function main()
{
	loadTopbar(document.getElementById("topbarcontainer"));
}

function visualize(logdata)
{
	let wheelFL = document.getElementById("wheelFL");
	let wheelFR = document.getElementById("wheelFR");
	let wheelRL = document.getElementById("wheelRL");
	let wheelRR = document.getElementById("wheelRR");

	let datalines = logdata.split('\n');

	for (i in datalines) {
		let time = datalines[i].split(' | ')[0];
		var value = datalines[i].split(' | ')[1];
		console.log(value);

		if(value.split(' ')[0] == "setSteer") {
			let turnvalue = (value.split(' ')[1] - 1500) / 10;
			wheelFL.style.transform = `rotate(${turnvalue}deg)`;
			wheelFR.style.transform = `rotate(${turnvalue}deg)`;
		}
	}
}

const fileInput = document.getElementById('fileInput');

fileInput.addEventListener('change', (event) =>
{
	const file = event.target.files[0];
	const reader = new FileReader();
	reader.onload = () =>
	{
		const content = reader.result;
		visualize(content);
	};
	reader.readAsText(file);
});

main();
