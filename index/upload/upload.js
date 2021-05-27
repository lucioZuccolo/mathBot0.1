const logout = document.querySelector('click', e =>{
  e.preventDefault();
  auth.signOut().then(() => {
    console.log("log out");
    document.location.href="./index/index.html";
  })
})

/* ######## upload file ########## */


document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
    const dropZoneElement = inputElement.closest(".drop-zone");
  
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
  
/* ######## end upload file ########## */

var userList = []
var thisWeekList = []

let xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    let data = JSON.parse(this.responseText).feed.entry;

    let i;
    for (i = 0; i < data.length; i++) {
      let user = data[i]["gsx$_cn6ca"]["$t"];
      let thisWeek = data[i]["gsx$_cokwr"]["$t"];

      userList.push([user, thisWeek])

      document.getElementById("demo").innerHTML +=
        "<tr>" +
        "<td>" +
        user +
        "</td>" +
        "<td>" +
        thisWeek +
        "</td>" +
        "</tr>";
      }
    }
};


  /**
   * Updates the thumbnail on a drop zone element.
   *
   * @param {HTMLElement} dropZoneElement
   * @param {File} file
   */
   function updateThumbnail(dropZoneElement, file) {
    let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");
  
    // First time - remove the prompt
    if (dropZoneElement.querySelector(".drop-zone__prompt")) {
      dropZoneElement.querySelector(".drop-zone__prompt").remove();
    }
  
    // First time - there is no thumbnail element, so lets create it
    if (!thumbnailElement) {
      thumbnailElement = document.createElement("div");
      thumbnailElement.classList.add("drop-zone__thumb");
      dropZoneElement.appendChild(thumbnailElement);
    }
  
    thumbnailElement.dataset.label = file.name;
  
    // Show thumbnail for image files
    if (file.type.startsWith("image/")) {
      const reader = new FileReader();
  
      reader.readAsDataURL(file);
      reader.onload = () => {
        thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
      };
    } else {
      thumbnailElement.style.backgroundImage = null;
    }
  }
  

xmlhttp.open(
  "GET",
  "https://spreadsheets.google.com/feeds/list/15BAZ5nBupYJdjwpBNnd5OvgR4xno0pEkQrsGhTvCPOw/od6/public/values?alt=json",
  true
);
xmlhttp.send();

/* ####### end ########*/

path = "prueba6.xlsx"
fee = 0
ryan = 0
zane = 0
austin = 0

var input = document.getElementById('input');
input.addEventListener('change', function(){
  readXlsxFile(input.files[0]).then(function(data){
    console.log(data);
  })

})