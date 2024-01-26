// Drop down for more images
document.getElementById('toggleButton').addEventListener('click', function() {
  const imageContainer = document.querySelector('.image-container');
  const images = document.querySelectorAll('.image');

  if (imageContainer.classList.contains('show')) {
    imageContainer.classList.remove('show');
    images.forEach(image => image.classList.remove('show'));
  } else {
    imageContainer.classList.add('show');
    images.forEach(image => image.classList.add('show'));

    // Hide images under #toggleButton2
    const imageContainer2 = document.querySelector('.image-container2');
    const images2 = document.querySelectorAll('.image2');
    imageContainer2.classList.remove('show');
    images2.forEach(image => image.classList.remove('show'));
  }
});

document.getElementById('toggleButton2').addEventListener('click', function() {
  const imageContainer = document.querySelector('.image-container2');
  const images = document.querySelectorAll('.image2');

  if (imageContainer.classList.contains('show')) {
    imageContainer.classList.remove('show');
    images.forEach(image => image.classList.remove('show'));
  } else {
    imageContainer.classList.add('show');
    images.forEach(image => image.classList.add('show'));

    // Hide images under #toggleButton
    const imageContainer1 = document.querySelector('.image-container');
    const images1 = document.querySelectorAll('.image');
    imageContainer1.classList.remove('show');
    images1.forEach(image => image.classList.remove('show'));
  }
});



// To enlarge images
document.querySelectorAll('.c-img').forEach(function(item) {
  item.addEventListener('click', function() {
    enlargeImage(item.src);
  });
});

// To enlarge images
document.querySelectorAll('.m-img').forEach(function(item) {
  item.addEventListener('click', function() {
    enlargeImage(item.src);
  });
});

// Function to open a modal with a larger image
function enlargeImage(src) {
  // Get the modal image element
  var modalImage = document.getElementById('modalImage');
  // Set the source of the modal image to the clicked image
  modalImage.src = src;
  // Create a new Bootstrap modal instance with options
  var imageModal = new bootstrap.Modal(document.getElementById('imageModal'), {
    keyboard: false,
  });
  // Show the modal
  imageModal.show();

  var closeButton = document.querySelector('#imageModal .btn-close');
    closeButton.addEventListener('click', function() {
      // Manually close the modal
      imageModal.hide();
    });
   // Add event listener for the escape key
   document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
      // Manually close the modal when the escape key is pressed
      imageModal.hide();
    }
  });
}