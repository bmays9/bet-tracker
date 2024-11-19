const updateButton = document.getElementById("submitUpdateBet");
const confirmRedirectButton = document.getElementById("confirmRedirectButton");
const updateConfModalElement = document.getElementById("updateConfModal");

console.log("JS")
console.log("JS Loaded");
console.log("Submit button:", updateButton);
console.log("Modal element:", updateConfModalElement);


updateButton.addEventListener("click", (e) => {
  updateConfModalElement.show();
  console.log("Modal shown")
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



/**
* Places an event listener on the save changes button on update_bet.html
* 
* Displays the modal 'updateConfModal'
* 
***/



  