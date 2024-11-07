// diagram chart
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
			maintainAspectRatio: false,
			scales: {
				y: {
					beginAtZero: true
				}
			}
		}
	});
}

// add a new datapoint to diagram chart
function addDataPoint(time = false, value, curve)
{
	const currentPoints = chart.data.datasets[curve].data.length;
	chart.data.datasets[curve].data.push(value);

	if (!(!time)) {
		let labels = chart.data.labels;
		labels.push(time.toFixed(3));
		chart.update();
	}
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
		// stop when file is at the end
		if(datalines[i].split(' | ')[0] == "") {
			addTerminal("logfile end", systemCurrentTime);
			break;
		}

		while (systemCurrentTime >= logCurrentTime) {
			// stop when file is at the end
			if(datalines[i].split(' | ')[0] == "") {
				addTerminal("logfile end", systemCurrentTime);
				break;
			}

			systemCurrentTime = (Date.now() / 1000) - systemStartTime;
			let logCurrentTime = parseFloat(datalines[i].split(' | ')[0]) - logStartTime;

			if (systemCurrentTime >= logCurrentTime) {
				var value = datalines[i].split(' | ')[1];

				if(value.split(' ')[0] == "setSteer") {
					let steervalue = value.split(' ')[1];
					let turnvalue = (steervalue - 1500) / 10;
					wheelFL.style.transform = `rotate(${turnvalue}deg)`;
					wheelFR.style.transform = `rotate(${turnvalue}deg)`;

					let steervaluePercent = parseInt((steervalue - 1000) / 10);
					timeField.innerHTML = `time: ${parseInt((datalines[i].split(' | ')[0]) - logStartTime)}s`;
					addDataPoint(false, steervaluePercent, 1);

				} else if(value.split(' ')[0] == "setSpeed") {
					let speedvalue = parseInt(((value.split(' ')[1] - 1000) / 10));
					if(speedvalue <= 0) {
						speedvalue = 0;
					}
					zitterDiv(wheelRL, speedvalue / 2);
					zitterDiv(wheelRR, speedvalue / 2);
					powerIndicator.innerHTML = `${speedvalue}%`;
					addDataPoint(logCurrentTime, speedvalue, 0);
				} else if(value == "armed") {
					startCheckbox.checked = true;
					addTerminal("armed", logCurrentTime);
				} else if(value == "disarmed") {
					startCheckbox.checked = false;
					addTerminal("disarmed", logCurrentTime);
				} else if(value.split(' ')[0] == "switched") {
					gearbox.innerHTML = `${value.split(' ')[3]}. gear`;
					addTerminal(`switched to ${value.split(' ')[3]}. gear`, logCurrentTime);
				} else if(value == "startInputScanner...") {
					addTerminal("start InputScanner", logCurrentTime);
					addTerminal("waiting for inputs...", logCurrentTime);
				} else if(value == "readMinMax...") {
					addTerminal("reading calibration values", logCurrentTime);
				} else if(value == "setupSteerPin...") {
					addTerminal("setup and prepare steering pin", logCurrentTime);
				} else if(value == "setupSpeedMotor...") {
					addTerminal("setup and prepare motor pin", logCurrentTime);
				} else if(value == "ready") {
					addTerminal("ready!", logCurrentTime);
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

function addTerminal(string, time)
{
	const textarea = document.getElementById("terminalTextarea");
	textarea.innerHTML += `${time.toFixed(2)}: ${string}\n`;
	textarea.scrollTop = textarea.scrollHeight;
}

main();
