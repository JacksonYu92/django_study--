function clickMe() {
    // 1.获取用户输入的内容
    var tag = document.getElementById("content");
    var userInputData = tag.value;

    // 2.找到div，并将内容赋值
    var tagTxt = document.getElementById("txt");
    tagTxt.innerText = userInputData;
}