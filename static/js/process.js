var fileInput = document.getElementById("inputFile");
fileInput.addEventListener("change", handleFileSelect, false);

var fileContent;
var fileResult = '';

function handleFileSelect(event) 
{
    var selectedFile = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function(e) {
        fileContent = e.target.result;
        document.getElementById('lblFileContent').innerText = fileContent;
    }

    reader.readAsText(selectedFile);
}
function onFileSelect() {
    var fileInput = document.getElementById("inputFile");
    fileInput.click();
}

function onFileProcess() {
    var contents = String(fileContent).split('\n');
    contents.forEach(content => {
        let numbers = content.match(/\d+/g); // Extract numbers from the string and create an array

        let updatedNumbers = numbers.map(num => parseInt(num) + 2); // Add 2 to each number in the array

        let updatedStr = "(" + updatedNumbers.join(", ") + ")\n"; // Convert the updated array back into a string
        fileResult += updatedStr;
    })
    document.getElementById('lblFileResult').innerText = fileResult;
}