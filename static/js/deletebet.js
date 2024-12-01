const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let betId = e.target.getAttribute("bet_id");
    deleteConfirm.href = `delete/${betId}`;
    deleteModal.show();
  });
}
  