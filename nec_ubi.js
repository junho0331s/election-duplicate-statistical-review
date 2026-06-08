/******************************************************************************
Description	: UbiReport 호출
Author		: 이유봉
Date		: 2018-03-20
Update      : 
******************************************************************************/
// UbiReport 호출
// title : 리포트 상단 제목
// arg :
// type : PRINT, PDF, EXCEL, HWP
var rep_pop_win;

String.prototype.replaceAll = function(org,dest){
	return this.split(org).join(dest);
	};

function go_Report(type)
{
	if($("table").find($("table tbody tr td:first:contains('검색된 결과가 없습니다.')")).length == 1) {
		alert("검색된 결과가 없습니다.");
		return false;
	} else {
		if($("#ubi_form").length==0){
			var frm = document.createElement("form");
			frm.name="ubi_form";
			frm.id="ubi_form";
			frm.method="POST";
			frm.action="/ubi4/ubihtml.jsp";
			$("body").append(frm);
			frm=$("#ubi_form");
			
			var inputArr = ["title", "arg", "tabledata", "type"];
			for(var i=0; i<4; i++){
				var ubiInp = "<input name='" + inputArr[i] + "'type='hidden'></input>";
				frm.append(ubiInp);
			}
			frm.append("<div id='rep_down'></div>");
		}
	
		fn_chkUbiData();
	
		var arg = "title#" + rTitle + "#condition#" + selectCondition + "#type#" + type + "#";
		//미리보기
		//rep_pop_win = window.open("", "rep_pop_win", "top=0,left=0,width=1152,height=768,resizable=no, scrollbars=no,menubars=no,status=no");
		//파일다운로드
		document.getElementById("rep_down").innerHTML = "<iframe name='rep_frame' src='' width='0' height='0' frameborder=0></iframe>";
	
		document.getElementById("ubi_form").title.value = fTitle;
		document.getElementById("ubi_form").arg.value = arg;
		document.getElementById("ubi_form").type.value = type;
	
		if(tabledata == "undefined") {
			tabledata = document.getElementById("tableWrapPostionA").innerHTML;
		}
	
		if(typeof(tabledata) == "string") {
			tabledata = tabledata.replaceAll("&nbsp;", " ");
			tabledata = tabledata.replaceAll("javascript", "");
			tabledata = tabledata.replaceAll("script", "");
		}

		document.getElementById("ubi_form").tabledata.value= tabledata;

		//미리보기
		//document.getElementById("ubi_form").target = 'rep_pop_win';
		//파일다운로드
		document.getElementById("ubi_form").target = 'rep_frame';
		document.getElementById("ubi_form").submit();
	}
}