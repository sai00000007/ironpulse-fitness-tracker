function validateBMI() {
    const height = document.querySelector("input[name='height']").value;
    const weight = document.querySelector("input[name='weight']").value;

    if (height <= 0 || weight <= 0) {
        alert("Height and Weight must be positive values");
        return false;
    }
    return true;
}

function dismissTip() {
    document.getElementById("splitTip").style.display = "none";
    localStorage.setItem("hideSplitTip", "true");
}

window.onload = function () {
    if (localStorage.getItem("hideSplitTip") === "true") {
        const tip = document.getElementById("splitTip");
        if (tip) tip.style.display = "none";
    }
};

