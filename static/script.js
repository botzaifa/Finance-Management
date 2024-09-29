document.addEventListener('DOMContentLoaded', function() {
    const calculateBtn = document.getElementById('calculateBtn');
    calculateBtn.addEventListener('click', function() {
      const loanAmount = parseFloat(document.getElementById('loanAmount').value);
      const interestRate = parseFloat(document.getElementById('interestRate').value) / 100;
      const loanTerm = parseFloat(document.getElementById('loanTerm').value) * 12;
  
      const monthlyInterest = interestRate / 12;
      const denominator = Math.pow(1 + monthlyInterest, loanTerm) - 1;
      const monthlyPayment = (loanAmount * monthlyInterest) / denominator;
  
      document.getElementById('monthlyPayment').textContent = `₹${monthlyPayment.toFixed(2)}`;
    });
  });

  function redirectToSignIn() {
    window.location.href = "signin.html"; // Change "signin.html" to the actual URL of your sign-in page
}

function redirectToSignUp() {
    window.location.href = "signup.html"; // Change "signup.html" to the actual URL of your sign-up page
}
