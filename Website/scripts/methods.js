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


const form = document.querySelector('.item-form');
form.addEventListener('submit', handleFormSubmit);

// Create a get request

fetch('https://6b97-130-113-109-194.ngrok.io/history',{method: 'GET', mode: 'no-cors'})
  // .then((response) => response.json())
  .then((json) => console.log(json));
