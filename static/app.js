const countDownDate = new Date();
countDownDate.setMinutes(countDownDate.getMinutes() + 5); // Example: 5 minutes from now


// Update the countdown every 1 second
const x = setInterval(function() {

  // Get the current date and time
  const now = new Date().getTime();

  // Calculate the remaining time
  const distance = countDownDate - now;

  // Calculate minutes and seconds
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the countdown
  document.getElementById("timer").innerHTML = minutes + "m " + seconds + "s ";

  // If the countdown is over, display a message
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("timer").innerHTML = "EXPIRED";
    // window.location.href = "{{ url_for('static', filename='/app.js') }}";
    // return render_template('expired.html')
    window.location.href = '/expired';

  }
}, 1000);


function getCursor(event) {
  let x = event.clientX;
  let y = event.clientY;
  let _position = `X: ${x}<br>Y: ${y}`

  console.log(_position);

  const infoElement = document.getElementById('info');
  infoElement.innerHTML = _position;
  infoElement.style.top = y + "px";
  infoElement.style.left = (x + 20) + "px";
  }
