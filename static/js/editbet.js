const updateButtons = document.getElementsByClassName("btn-edit");
const submitButton = document.getElementById("submitButton");


/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated bet ID upon click.
* - Fetches the content of the corresponding bet.
* - Populates the Bet and Line data with the necessary data.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_bet/{betId}` endpoint.
*/

for (let button of updateButtons) {
    button.addEventListener("click", (e) => {
      let betId = e.target.getAttribute("bet_id");
      let betContent = document.getElementById(`bet${betId}`).innerText;
      commentText.value = commentContent;
      submitButton.innerText = "Update";
      commentForm.setAttribute("action", `update_bet/${betId}`);
    });
  }