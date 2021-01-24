function editorChangeHandler(ed) {
  var content = tinyMCE.activeEditor.getContent();
  var contentLen = content.length;
  if (contentLen > 50) {
    var request = new XMLHttpRequest()

    request.open('POST', 'http://127.0.0.1:5000/text/', true)
    // request.setRequestHeader("Content-Type", "application/json");

    request.onreadystatechange = function () {
      if (request.readyState === 4 && request.status === 200) {
        var json = JSON.parse(request.responseText);
        console.log(json.code + ", " + json.distance);
      }
    };

    var data = JSON.stringify({"text": content});
    request.send(data)


    // var drgCode = document.getElementById("drgCode");
    // drgCode.innerText = "P57C";
    // drgCode.style.backgroundColor = "orange";
  }
}
