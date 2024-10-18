// Basic Form Validation
function validateForm() {
    const name = document.forms["registrationForm"]["name"].value;
    const email = document.forms["registrationForm"]["email"].value;
    const password = document.forms["registrationForm"]["password"].value;
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;  // Simple email regex

    if (name === "" || email === "" || password === "") {
        alert("All fields must be filled out");
        return false;
    }

    if (!re.test(email)) {
        alert("Please enter a valid email address");
        return false;
    }

    if (password.length < 6) {
        alert("Password must be at least 6 characters long");
        return false;
    }

    return true;
}

// AJAX for Submitting Feedback
function submitFeedback(event) {
    event.preventDefault();
    const feedbackText = document.getElementById('feedbackText').value;
    const teacherId = document.getElementById('teacherId').value;

    if (feedbackText === "") {
        alert("Feedback cannot be empty");
        return;
    }

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/submit_feedback", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    xhr.onload = function () {
        if (xhr.status === 200) {
            alert("Feedback submitted successfully!");
            document.getElementById('feedbackForm').reset();
        } else {
            alert("An error occurred. Please try again.");
        }
    };

    xhr.send("teacherId=" + teacherId + "&feedbackText=" + feedbackText);
}

// Toggle Modals for Teacher Details
function toggleModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.style.display = (modal.style.display === "block") ? "none" : "block";
}

window.onclick = function (event) {
    const modals = document.getElementsByClassName('modal');
    Array.from(modals).forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
}
