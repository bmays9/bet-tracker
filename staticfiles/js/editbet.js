const updateButton = document.getElementById("submitUpdateBet");
const settleButton = document.getElementById("submitSettleBet");
const confirmRedirectButton = document.getElementById("confirmRedirectButton");
var betStatusElement = document.getElementById("id_status");
var betStakeElement = document.getElementById("id_stake");
var betSettledElement = document.getElementById("id_settled_amount");
const updateConfModalElement = document.getElementById("updateConfModal");
const settledBetModalElement = document.getElementById("settledBetModal");
var settleBetWarning = document.getElementById("settleBetWarning");
var updateBetInfo = document.getElementById("updateBetInfo");

console.log("JS");
console.log("JS Loaded");
console.log(settleBetWarning);
console.log(settleBetWarning.innerText);

console.log("Submit button:", updateButton);
console.log("Modal element:", updateConfModalElement);

/**
 * Places an event listener on the save changes button on update_bet.html
 * 
 * If the bet is still pending: displays the modal 'updateConfModal'
 * If the bet is settled: displays the modal 'settledBetModal'
 **/

updateButton.addEventListener("click", (e) => {
    updateConfModalElement.show();
});

settleButton.addEventListener("click", (e) => {
  settledBetModalElement.show();
});



betStatusElement.addEventListener("change", (e) => {
    console.log("you changed it");
    var betStatus = betStatusElement.value;
    var stakeAmount = betStakeElement.value;
    var settledAmount = betSettledElement.value;

    if (betStatus == '0') {
        /* Bet status is pending */
        console.log("Now PENDING");
        updateButton.disabled = false;
        settleButton.disabled = true;
        settleBetWarning.textContent = "Bet status is pending.";
        updateBetInfo.textContent = "Saving changes will not alter your balance and the bet will remain open.";
    } else if (betStatus == '1') {
        /* Bet status is win */
        console.log("WINNER");
        if (parseFloat(settledAmount) < parseFloat(stakeAmount)) {
            updateButton.disabled = true;
            settleButton.disabled = true;
            settleBetWarning.textContent = "This cannot be a winning bet. Settled amount is lower than the stake.";  
            updateBetInfo.textContent = "To continue, please change the bet status to Lose";
        } else {
        updateButton.disabled = true;
        settleButton.disabled = false;
        settleBetWarning.textContent = "Please check all bet lines are correct. No changes are possible once the bet is closed.";
        updateBetInfo.textContent = "Saving now will settle the bet as a WINNER, with a return of £" + settledAmount;
        }
    } else {
        /* Bet status is lose */
        if (parseFloat(settledAmount) > parseFloat(stakeAmount)) {
            updateButton.disabled = true;
            settleButton.disabled = true;
            settleBetWarning.textContent = "This cannot be a losing bet. Settled amount is greater than the stake.";  
            updateBetInfo.textContent = "To continue, please change the bet status to Win";

        
        } else {
            updateButton.disabled = true;
            settleButton.disabled = false;
            settleBetWarning.textContent = "Please check all bet lines are correct. No changes are possible once the bet is closed.";
            updateBetInfo.textContent = "Saving now will settle as a losing bet.";
        }
    }
});

/**
 * Show confirmation of updates Modal. Redirect user to the homepage
 */
if (updateConfModalElement && updateConfModalElement.dataset.show === "true") {
    console.log("Success");
    const successModal = new bootstrap.Modal(updateConfModalElement);
    successModal.show();

    // Redirect when the user clicks the OK button
    confirmRedirectButton.addEventListener("click", () => {
        window.location.href = '/bets/';
    });
}

/**
 * Show confirmation of updates Modal. Redirect user to the homepage
 */
if (settledBetModalElement && settledBetModalElement.dataset.showSettle === "true") {
    console.log("Save Success");
    const settledModal = new bootstrap.Modal(settledBetModalElement);
    settledModal.show();

    // Redirect when the user clicks the OK button
    confirmRedirectButton.addEventListener("click", () => {
        window.location.href = '/bets/';
    });
}
