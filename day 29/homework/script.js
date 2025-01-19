document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');

    registerForm.addEventListener('submit', function(event) {
        event.preventDefault(); // ფორმის გაგზავნის თავიდან აცილება

        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        if (password !== confirmPassword) {
            alert('პაროლები არ ემთხვევა.');
            return;
        }

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;

        alert(`რეგისტრაცია წარმატებით განხორციელდა!\nმომხმარებელი: ${name}\nელ. ფოსტა: ${email}`);
    });
});
