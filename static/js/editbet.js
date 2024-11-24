const updateButton = document.getElementById("submitUpdateBet");
const confirmRedirectButton = document.getElementById("confirmRedirectButton");
const updateConfModalElement = document.getElementById("updateConfModal");
const lineStatus = document.getElementsByTagName("select");

console.log(lineStatus)
console.log("JS")
console.log("JS Loaded");
console.log("Submit button:", updateButton);
console.log("Modal element:", updateConfModalElement);
/**
* Places an event listener on the save changes button on update_bet.html
* 
* Displays the modal 'updateConfModal'
* 
***/

updateButton.addEventListener("click", (e) => {
  isSettled = isBetSettled()
  updateConfModalElement.show();
   });
  
if (updateConfModalElement && updateConfModalElement.dataset.show === "true") {
  console.log("Success")
  const successModal = new bootstrap.Modal(updateConfModalElement);
  successModal.show();

  // Redirect when the user clicks the OK button
  confirmRedirectButton.addEventListener("click", () => {
      window.location.href = '/'; 
  });
}

function isSettled(){
  console.log("lineStatus")
  
}

/**
* Checks the form data to see if the bet is settled
* Returns True if settled, false if any line is still pending.
**/









  