# nBajax_request

这是一个很牛逼的ajax跨域教程
json的手动编写：
手动实现jsonp

function funcvvvvvv(arg) {
    alert(arg);

    document.head.removeChild(tag);
}

function jsonp(url){
    tag = document.createElement('script');
    tag.src = url;
    document.head.appendChild(tag);

views
def index(request):
    response = requests.get('http://127.0.0.1:8000/get_data.html')
    return render(request,'index.html',{'response':response})


使用jquery的：

function Jsonp2(){
    $.ajax({
        url: "http://127.0.0.1:8000/get_data.html",
        type: 'GET',
        dataType: 'JSONP',
        success: function(data){
            console.log(data);
        }
    })
}

function list(arg) {
    console.log(arg);
}
function Jsonp3(){
    $.ajax({
        url: "http://www.jxntv.cn/data/jmd-jxtv2.html",
        type: 'GET',
        dataType: 'JSONP',
        jsonp: 'callback',//定义callback头
        jsonpCallback: 'list' //定义函数名称
    })
}

jsonp只能发get请求本质就是一个script标签 通过src获取数据


cors：
def get_data(request):
    if request.method == "OPTIONS":
        # 预检
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = "*"
        # response['Access-Control-Allow-Methods'] = "PUT"
        response['Access-Control-Allow-Headers'] = "xxx"
        return response

    elif request.method == "GET":
        response = HttpResponse("机密数据")
        response['Access-Control-Allow-Origin'] = "*"

        return response
		
		
		
应用场景：
	 你，调用者
	CEO，服务商，提供API
	
	- JSONP交互
	- requests模块
	
	
	用户，调用者
	  你，服务商，提供API
	  
	  专业：获取用户请求callback，func(内容)

JSONP是否可以发送POST请求？