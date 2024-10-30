function main()
{
	loadTopbar(document.getElementById("topbarcontainer"));
}

async function visualize(logdata)
{
	const wheelFL = document.getElementById("wheelFL");
	const wheelFR = document.getElementById("wheelFR");
	const wheelRL = document.getElementById("wheelRL");
	const wheelRR = document.getElementById("wheelRR");

	const datalines = logdata.split('\n');

	const systemStartTime = parseFloat(Date.now()) / 1000;
	let systemCurrentTime = (parseFloat(Date.now()) / 1000) - systemStartTime;

	const logStartTime = parseFloat(datalines[0].split(' | ')[0]);
	let logCurrentTime = parseFloat(datalines[0].split(' | ')[0]) - logStartTime;

	for (i in datalines) {
		console.log(systemCurrentTime >= logCurrentTime);
		while (systemCurrentTime >= logCurrentTime) {
			// stop when file is at the end
			if(datalines[i].split(' | ')[0] == "") {
				break;
			}


			systemCurrentTime = (Date.now() / 1000) - systemStartTime;
			let logCurrentTime = parseFloat(datalines[i].split(' | ')[0]) - logStartTime;

			console.log("systemCurrentTime: " + systemCurrentTime);
			console.log("logCurrentTime: " + logCurrentTime);
			console.log(systemCurrentTime >= logCurrentTime);
			console.log("-------------")

			if (systemCurrentTime >= logCurrentTime) {
				var value = datalines[i].split(' | ')[1];

				if(value.split(' ')[0] == "setSteer") {
					let turnvalue = (value.split(' ')[1] - 1500) / 10;
					wheelFL.style.transform = `rotate(${turnvalue}deg)`;
					wheelFR.style.transform = `rotate(${turnvalue}deg)`;
				}

				break;
			}

			await new Promise(resolve => setTimeout(resolve, 50));
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

function sleep(ms)
{
	var start = new Date().getTime(), expire = start + ms;
	while (new Date().getTime() < expire) { }
	return;
}

main();
