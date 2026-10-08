// Model
const model = {
  name: "João",
  idade: 17
};

// ViewModel
const viewModel = {
  name: model.name,

  changeName() {

    if (this.name === "João") {
      this.name = "Maria";
    }
    else {
      this.name = "João";
    }

    render();
  }
};

// View
function render() {
  document.querySelector("#name").textContent = viewModel.name;
}

document.querySelector("#btn").addEventListener("click", () => {
  viewModel.changeName();
});

render();