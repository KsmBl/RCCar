const ctx = document.getElementById('lineChart').getContext('2d');
let chart = null;

function main()
{
	loadTopbar(document.getElementById("topbarcontainer"));

	chart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: [],
			datasets: [{
					label: 'Speed',
					data: [],
					borderColor: 'rgb(0, 0, 0)',
					tension: 0.1
				},

				{
				label: 'Steer',
				data: [],
				borderColor: 'rgb(255, 255, 0)',
				tension: 0.1
				}]
		},
		options: {
			responsive: true,
			scales: {
				y: {
					beginAtZero: true
				}
			}
		}
	});
}

function addDataPoint(time, value, curve)
{
	const currentPoints = chart.data.datasets[curve].data.length;
	chart.data.datasets[curve].data.push(value);
	chart.data.labels.push(time);
	chart.update();
}

async function visualize(logdata)
{
	const wheelFL = document.getElementById("wheelFL");
	const wheelFR = document.getElementById("wheelFR");
	const wheelRL = document.getElementById("wheelRL");
	const wheelRR = document.getElementById("wheelRR");
	const timeField = document.getElementById("time");
	const powerIndicator = document.getElementById("powerIndicator");
	const startCheckbox = document.getElementById("startCheckbox");
	const gearbox = document.getElementById("gearBox");

	const datalines = logdata.split('\n');

	const systemStartTime = parseFloat(Date.now()) / 1000;
	let systemCurrentTime = (parseFloat(Date.now()) / 1000) - systemStartTime;

	const logStartTime = parseFloat(datalines[0].split(' | ')[0]);
	let logCurrentTime = parseFloat(datalines[0].split(' | ')[0]) - logStartTime;

	for (i in datalines) {
		
		if(datalines[i].split(' | ')[1].split(' ')[0] == "setSpeed") {
			let speedvalue = parseInt(((datalines[i].split(' | ')[1].split(' ')[1] - 1000) / 10));
			if(speedvalue <= 0) {
				speedvalue = 0;
			}
			timeField.innerHTML = `time: ${parseInt((datalines[i].split(' | ')[0]) - logStartTime)}s`;
			addDataPoint(systemCurrentTime, speedvalue, 0);
		} else if(datalines[i].split(' | ')[1].split(' ')[0] == "setSteer") {
			let steervalue = parseInt(((datalines[i].split(' | ')[1].split(' ')[1] - 1000) / 10));
			timeField.innerHTML = `time: ${parseInt((datalines[i].split(' | ')[0]) - logStartTime)}s`;
			addDataPoint(systemCurrentTime, steervalue, 1);
		}

		while (systemCurrentTime >= logCurrentTime) {
			// stop when file is at the end
			if(datalines[i].split(' | ')[0] == "") {
				console.log("end");
				break;
			}

			systemCurrentTime = (Date.now() / 1000) - systemStartTime;
			let logCurrentTime = parseFloat(datalines[i].split(' | ')[0]) - logStartTime;

			if (systemCurrentTime >= logCurrentTime) {
				var value = datalines[i].split(' | ')[1];

				if(value.split(' ')[0] == "setSteer") {
					let turnvalue = (value.split(' ')[1] - 1500) / 10;
					wheelFL.style.transform = `rotate(${turnvalue}deg)`;
					wheelFR.style.transform = `rotate(${turnvalue}deg)`;
				} else if(value.split(' ')[0] == "setSpeed") {
					let speedvalue = parseInt(((value.split(' ')[1] - 1000) / 10));
					if(speedvalue <= 0) {
						speedvalue = 0;
					}
					zitterDiv(wheelRL, speedvalue / 2);
					zitterDiv(wheelRR, speedvalue / 2);
					powerIndicator.innerHTML = `${speedvalue}%`;
				} else if(value == "armed") {
					startCheckbox.checked = true;
				} else if(value == "disarmed") {
					startCheckbox.checked = false;
				} else if(value.split(' ')[0] == "switched") {
					gearbox.innerHTML = `${value.split(' ')[3]}. gear`;
				}

				break;
			}

			await new Promise(resolve => setTimeout(resolve, 25));
		}
	}

	timeField.innerHTML = "time: end";
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

function zitterDiv(element, strength)
{
	const offset = Math.random() * strength - (strength / 2);
	element.style.transform = `translate(${offset / 3}px, ${offset / 2}px)`;
}

main();
