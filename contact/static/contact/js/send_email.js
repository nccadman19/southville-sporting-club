// (function () {
//     emailjs.init("YDEgGEzmSaGegV1jm");

//     // Define the sendMail function outside the event listener
//     function sendMail() {
//         var name = document.getElementById("name").value;
//         var email = document.getElementById("email").value;
//         var message = document.getElementById("subject").value;

//         var params = {
//             from_name: name,
//             from_email: email,
//             message: message
//         };

//         emailjs.send("service_0n83z1k", "template_3de9a7t", params)
//             .then(function (res) {
//                 // Set a success message in the Django session
//                 document.cookie = "success_message=Your message has been successfully sent!";
//                 var form = document.getElementById("contactForm");
//                 form.submit();  // Submit the form to trigger the Django view
//             })
//             .catch(function (error) {
//                 console.log("Failed to send the email:", error);
//             });
//     }

//     // Attach the event listener to the form
//     document.getElementById("contactForm").addEventListener("submit", function (event) {
//         event.preventDefault();
//         // Call the sendMail function when the form is submitted
//         sendMail();
//     });
// })();
