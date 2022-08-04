let upload = () => {
    let progressValue = document.querySelector('.progress-value'),
    progress = document.querySelector('.progress')
    progressValue.setAttribute('id', 'play-animation')
    
    progress.style.opacity = 1
}


// FOR DROP DOWN
document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
    const dropZoneElement = inputElement.closest(".break_line_rectangle");
  
    dropZoneElement.addEventListener("click", (e) => {
      inputElement.click();
    });
  
    inputElement.addEventListener("change", (e) => {
      if (inputElement.files.length) {
        updateThumbnail(dropZoneElement, inputElement.files[0]);
      }
    });
  
    dropZoneElement.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropZoneElement.classList.add("drop-zone--over");
    });
  
    ["dragleave", "dragend"].forEach((type) => {
      dropZoneElement.addEventListener(type, (e) => {
        dropZoneElement.classList.remove("drop-zone--over");
      });
    });
  
    dropZoneElement.addEventListener("drop", (e) => {
      e.preventDefault();
  
      if (e.dataTransfer.files.length) {
        inputElement.files = e.dataTransfer.files;
        updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
      }
  
      dropZoneElement.classList.remove("drop-zone--over");
    });
  });
  

  function updateThumbnail(dropZoneElement, file) {

    
    let progressValue = document.querySelector('.progress-value'),
    progress = document.querySelector('.progress')
    progressValue.setAttribute('id', 'play-animation')
    
    progress.style.opacity = 1

    let upload_text = document.querySelector('.upload_text')

    upload_text.style.opacity = 1


    let thumbnailElement = dropZoneElement.querySelector(".progress-value", ".upload_text");

    // First time - remove the the initial prompt
    if (dropZoneElement.querySelector(".break_line_content")) {
      dropZoneElement.querySelector(".break_line_content").remove();
    }

  
    // First time - uploading and progress bar made visible
    if (!thumbnailElement) {
      thumbnailElement = document.createElement("div");
      thumbnailElement.classList.add("drop-zone__thumb");
      dropZoneElement.appendChild(thumbnailElement);
    }
  
    thumbnailElement.dataset.label = file.name;
}