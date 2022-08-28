const remDays = document.getElementById("days");
const remHours = document.getElementById("hours");
const remMinutes = document.getElementById("minutes");
const remSeconds = document.getElementById("seconds");

const birthDays = document.getElementById('times').innerText;

const birthDay = new Date(birthDays).getTime()

const formatTime = (time) => (time < 10 ? `0${time}` : time);

const countdown = () => {
  const birthDayDate = new Date(birthDay);
  const currentDate = new Date();

  const totalSeconds = (birthDayDate - currentDate) / 1000;

  const days = Math.floor(totalSeconds / 3600 / 24);
  const hours = Math.floor(totalSeconds / 3600) % 24;
  const mins = Math.floor(totalSeconds / 60) % 60;
  const seconds = Math.floor(totalSeconds) % 60;

  remDays.innerHTML = days;
  remHours.innerHTML = formatTime(hours);
  remMinutes.innerHTML = formatTime(mins);
  remSeconds.innerHTML = formatTime(seconds);
};
// initial call
countdown();

setInterval(countdown, 1000);


//deposit button event handler
const deposit_btn = document.getElementById('deposit-btn');
deposit_btn.addEventListener('click', function () {

  const depositStringToInt = getInputNumb("deposit-amount");

  updateSpanTest("current-deposit", depositStringToInt);
  updateSpanTest("current-balance", depositStringToInt);

  //setting up the input field blank when clicked
  document.getElementById('deposit-amount').value = "";

})

//withdraw button event handler
const withdraw_btn = document.getElementById('withdraw-btn');
withdraw_btn.addEventListener('click', function () {
  const withdrawNumb = getInputNumb("withdraw-amount");

  updateSpanTest("current-withdraw", withdrawNumb);
  updateSpanTest("current-balance", -1 * withdrawNumb);
  //setting up the input field blank when clicked
  document.getElementById('withdraw-amount').value = "";
})

//function to parse string input to int
function getInputNumb(idName) {
  const amount = document.getElementById(idName).value;
  const amountNumber = parseFloat(amount);
  return amountNumber;
}




