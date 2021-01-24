function editorChangeHandler(ed) {
  var content = tinyMCE.activeEditor.getContent({format: 'text'});
  var contentLen = content.length;
  var drgCode = document.getElementById("drgCode");

  if (contentLen > 30) {
    var request = new XMLHttpRequest()

    request.open('POST', 'http://64.225.96.72:5001/text/', true)
    // request.setRequestHeader("Content-Type", "application/json");

    request.onreadystatechange = function () {
      if (request.readyState === 4 && request.status === 200) {
        var json = JSON.parse(request.responseText);
        console.log(json.code + ", " + json.distance);

        drgCode.innerText = json.code;
        var color = "#e7e5e5";

        if (json.distance < 0.6) {
          color = "orange";
        }

        if (json.distance < 0.3) {
          color = "lime";
        }
        drgCode.style.backgroundColor = color;
      }
    };

    var data = JSON.stringify({"text": content});
    request.send(data)


  } else {
    drgCode.style.innerText = "?"
    drgCode.style.backgroundColor = "#e7e5e5";
  }
}
