// 刷新页面时间 (秒)
var timeout = 5;
// content直接复制进你的数据
var content = "shit";

// 获取当前的URL
var current = location.href;

// 提交代码--function
submit_data = function() {
  $("textarea")[1].value = content;
  // 提交数据
  $(".submit").click();
};

// 刷新页面--function
function reload() {
  // 下面两行代码的格式化后的内容为：
  // <frameset cols='*'>
  //     <frame src='当前地址栏的URL' />
  // </frameset>
  const fr4me = "<frameset cols='*'>\n<frame src='" + current + "' />";
  fr4me += "</frameset>";

  with (document) {
    // 引用document对象，调用write方法写入框架，打开新窗口
    write(fr4me);
    submit_data();
    // 关闭上面的窗口
    void close();
  }
}
setTimeout("reload()", 1000 * timeout);
