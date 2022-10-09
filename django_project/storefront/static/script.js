// form = document.querySelector("form");
console.log("hell0")
const submit_btn = document.getElementById("submit_ho_ja_bhai");
if (submit_btn){console.log("sdubvsd")};

submit_btn.onclick = function() {
    console.log("kjfekvbhkv")
    const name1 = document.getElementById("name").value;
    const pwd1 = document.getElementById("pwd").value;

    const dict_v = {'name': name1, 'pwd': pwd1};

    // const s = JSON.stringify(dict_v);

    // console.log(s)
    var URL = "{% url 'some_calc' %}";

    $.post(URL, dict_v);
    
};
