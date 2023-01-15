// Form submissions

// posting
async function postData(url = ' ', data = {}){
  const response = await fetch(url, {
    method: 'POST',
    mode: 'no-cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(data)
  });
  console.log(response)
  return response.text();
}



function handleFormSubmit(event) {
  // console.log("worked");
  event.preventDefault();

  const data = new FormData(event.target);

  const formJSON = Object.fromEntries(data.entries());

  // for multi-selects, we need special handling
  // formJSON.snacks = data.getAll('snacks');

  console.log(formJSON);

  postData('https://6b97-130-113-109-194.ngrok.io/registeralert', formJSON)

  .then((data) => {
    console.log(data);
  });
}

console.log("hello")
const form = document.querySelector('.item-form');
form.addEventListener('submit', handleFormSubmit);

// Create a get request
const historyBtns = document.getElementsByClassName('history_btn')

for(let i = 0; i < historyBtns.length; i++) {

  historyBtns[i].addEventListener('click', retrieve_data);
}

function retrieve_data(event){
  console.log("in retrive data function")
  getData('https://6b97-130-113-109-194.ngrok.io/tracking')
}

async function getData(url = ' '){
  console.log("in get Data")
  await fetch(url, {
    method: 'GET',
    // mode: 'no-cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
  })
  .then(function(response){
    return response.json();
  })
  .then(function(data){
    appendData(data);
    console.log(data);
  })
  // console.log(response)
  // return response.json();
}

function appendData(data) {
  // make it pretty: https://www.w3schools.com/html/html_tables.asp
  console.log("in append data")
  var mainContainer = document.getElementById("myData");
  console.log("date length "+data.length)
  for (var i = 0; i < data.length; i++) {
    var div = document.createElement("div");
    div.innerHTML = 'Item: ' + data[i].name + ' Platform: ' + data[i].platform + ' Buy Price ' + data[i].price;
    mainContainer.appendChild(div);
  }
}


// original code
// await fetch('https://6b97-130-113-109-194.ngrok.io/history',{method: 'GET', mode: 'no-cors'})
//   // .then((response) => response.json())
//   .then((incoming_data) => console.log(incoming_data));
