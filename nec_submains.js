//script file import
document.write( "<script type='text/javascript' src='/common/js/common.js?ver=240321'></script>");

// onload 
$(function () {
	
	var ua = window.navigator.userAgent.toLocaleLowerCase();
	
	// mobile
	/*if(/iphone/.test(ua) || /android/.test(ua) || /opera/.test(ua) || /bada/.test(ua) ) {
		// 최근선거 : 탑 메뉴 이벤트 함수
		fn_menu_mobile();
		
		// 역대선거 : 탑 메뉴 이벤트
		fn_preMenu_mobile();
	} else {
	*/
	
		// 최근선거 : 탑 메뉴 이벤트 함수
		fn_menu();
		
		// 역대선거 : 탑 메뉴 이벤트
		fn_preMenu();
	//}
	
	
	// 동적 메뉴 높이 설정 함수
	fn_dynamicHeight();
});

//최근선거 : 메인 메뉴 이벤트 함수
function fn_menu(){
	$('#menu li').bind('click', function() {
	     $(this).addClass('on').siblings().removeClass();
	     $('#allmenu').hide();
	});
	
	$('.submu li').bind('mouseover', function() {
	     $('#allmenu').show();
	});
	
	$('.submu li').bind('mouseleave', function() {
	
		$('#allmenu').hide();
		
		$('#allmenu').bind('mouseover', function() {
		  $('#allmenu').show();
		});  
	});
	
	$('#allmenu').bind('mouseleave', function() {
		$('#allmenu').hide();
	});
}

//역대선거 : 메인 메뉴 이벤트 함수
function fn_preMenu(){
	$( '#presubmu li' ).bind( 'mouseover', function() {
	     $( '#preallmenu' ).show();
	});
	
	$( '#presubmu li' ).bind( 'mouseleave', function() {
	
		$( '#preallmenu' ).hide();
		
		$( '#preallmenu' ).bind( 'mouseover', function() {
		  $( '#preallmenu' ).show();
		});  
	});
	
	$( '#preallmenu' ).bind( 'mouseleave', function() {
		$( '#preallmenu' ).hide();
	});
}


//최근선거 : 메인 메뉴 이벤트 함수
function fn_menu_mobile(){
	
	$('.submu.m li').bind('click', function() {
		if(strOpenMenuId == '') 
			strOpenMenuId = $( this ).children( 'a' ).attr( 'class' );

		if( strOpenMenuId == $( this ).children( 'a' ).attr( 'class' ) ) {

			if( $('#allmenu').css( 'display' ) != 'none' ){
				$('#allmenu').hide();
				
				strOpenMenuId = '';
			} else {
				$('#allmenu').show();
			}
		} else {
			$('#allmenu').show();
		}
	});
}

//역대선거 : 메인 메뉴 이벤트 함수
function fn_preMenu_mobile(){
	$('.presubmu.m li').bind('click', function() {
		if(strOpenPreMenuId == '') 
			strOpenPreMenuId = $( this ).children( 'a' ).attr( 'class' );

		if( strOpenPreMenuId == $( this ).children( 'a' ).attr( 'class' ) ) {

			if( $('#preallmenu').css( 'display' ) != 'none' ){
				$('#preallmenu').hide();
				
				strOpenPreMenuId = '';
			} else {
				$('#preallmenu').show();
			}
		} else {
			$('#preallmenu').show();
		}
	});
}

//사이드메뉴 레이어팝업  
function fn_layerPopUp( psrtDivId ){

	var temp = $( '#' + psrtDivId );		//레이어의 id를 temp변수에 저장
	var bg = temp.prev().hasClass( 'bg' );	//dimmed 레이어를 감지하기 위한 boolean 변수

	//기존에 떠있는 레이어 닫기
	$('.detail').fadeOut();

	if(bg){
		$( '#' + psrtDivId ).fadeIn();
	}else{
		temp.fadeIn();	//bg 클래스가 없으면 일반레이어로 실행한다.
	}

	temp.find('a.cbtn').click(function(e){
		if(bg){
			$( '#' + psrtDivId ).fadeOut();
		}else{
			temp.fadeOut();		//'닫기'버튼을 클릭하면 레이어가 사라진다.
		}
		 
		e.preventDefault();
	});

	$( '#' + psrtDivId + ' .bg' ).click(function(e){
		$( '#' + psrtDivId).fadeOut();
		e.preventDefault();
	});
	
	$('.detail').bind('mouseleave', function() {
		$('.detail').hide();
	});
}

/**
 * 동적메뉴 높이 제어 함수
 * @since  2015-12-10
 * @modify 2015-12-17
 */
function fn_dynamicHeight(){
	maxCnt = 0;
	maxHeight = 0;
/*
	for(var i = 0; i < $('#allmenu .allview li dl').size(); i++ ){
		if( maxCnt <= $('#allmenu .allview dl:eq(' + i + ')').children('dd').size() ) {
			maxHeight = 0;

			maxCnt = $('#allmenu .allview dl:eq(' + i + ')').children('dd').size();

			dlSize = $('#allmenu .allview dl:eq(' + i + ')').children('dd').size();

			for(var j = 0; j < dlSize; j++ ){
				if( $('#allmenu .allview dl:eq(' + i + ')').children('dd').eq(j).text().length > 11) {
					maxHeight++;
				}
			}
		}
	}

	//210812_ 수정 : 헤더 올 메뉴 li 높이 조정.
	$( '#allmenu .allview li' ).css( 'height', ( ( (maxCnt - maxHeight) * 36 ) + ( maxHeight * 44 ) ) + 'px' );
*/

	for(var i = 0 ; i < $('.gnb_area .gnblist > li').size() ; i++){
		if(maxCnt <= $('.gnb_area .gnblist > li:eq('+ i +') .sub_menu li').size()){
			maxheight = 0;
			
			maxCnt = $('.gnb_area .gnblist > li:eq('+ i +') .sub_menu li').size();
			
			dlSize = $('.gnb_area .gnblist > li:eq('+ i +') .sub_menu li').size();
			
			for(var j = 0 ; j < dlSize ; j++){
				if($('.gnb_area .gnblist > li:eq('+ i +') .sub_menu li').eq(j).text().length > 12){
					maxHeight++;
				}
			}
		}
	}
	
	$('.gnb_area .gnblist > li .sub_menu').css( 'height', ( ( (maxCnt - maxHeight) * 36 ) + ( maxHeight * 44 )) + 'px' );	
	$('.gnb_bg').css( 'height', ( (( (maxCnt - maxHeight) * 36 ) + ( maxHeight * 44 ))+32) + 'px' );
}

/**
 * 엑셀 다운로드 함수
 * @since  2016-01-18
 * @modify 2016-01-29
 */
function listFileDownload( pStrFileName, pStrFileType ){

	var url = "";
	var labelString = "";
	
	if( pStrFileType == "xls" ) { 
		url = "/listFileDown/electionInfo_download.xls"; 
	} else if( pStrFileType == "hwp" ) {
		url = "/listFileDown/electionInfo_download.hwp"; 
	} else if( pStrFileType == "pdf" ) {
		url = "/listFileDown/electionInfo_download.pdf"; 
	}
	
	// 검색 조건에 따른 label 처리 << 추가 필요함
	labelString += retrieveSelectedName('electionType') + ' ';
	labelString += retrieveSelectedName('electionName') + ' ';
	labelString += retrieveSelectedName('electionCode') + ' ';
	labelString += retrieveSelectedName('cityCode') + ' ';
	labelString += retrieveSelectedName('townCode') + ' ';
	labelString += retrieveSelectedName('sggCityCode') + ' ';
	labelString += retrieveSelectedName('sggTownCode') + ' ';
	
	/**
	 * 2016-01-29 추가
	 * Ubi Report일 시에는 ubiviewer.js function 실행. 
	 * search label 때문에 이곳에서 호출 처리 >> search label 표출 안됨, ubi report form 다시 그려야 함.
	 */
	if( pStrFileType == "report" ){
		go_Report( pStrFileName, labelString, "N");
		return;
	}
	
	if( pStrFileType != "print" ) {
		
		// form 생성
		var crtForm = window.document.createElement("form");
		crtForm.setAttribute('method', 'POST');
		crtForm.setAttribute('action', url);
		crtForm.setAttribute('accept-charset', 'uft-8');
		
		this.document.body.appendChild(crtForm);
		
		// input 생성 > file name set 
		var crtInput1 = window.document.createElement("input");
		crtInput1.setAttribute('type', 'hidden');
		crtInput1.setAttribute('name', 'dwFileName');
		crtInput1.setAttribute('value', pStrFileName);
	
		crtForm.appendChild(crtInput1);
		
		// input 생성 > table content set
		crtInput1 = window.document.createElement("input");
		crtInput1.setAttribute('type', 'hidden');
		crtInput1.setAttribute('name', 'dwContent');
		crtInput1.setAttribute('value', $('.cont_table').html());
		
		crtForm.appendChild(crtInput1);
		
		// input 생성 > search condition label set
		crtInput1 = window.document.createElement("input");
		crtInput1.setAttribute('type', 'hidden');
		crtInput1.setAttribute('name', 'labelString');
		crtInput1.setAttribute('value', labelString);
		
		crtForm.appendChild(crtInput1);
		
		// input 생성 > download file type set 
		var crtInput1 = window.document.createElement("input");
		crtInput1.setAttribute('type', 'hidden');
		crtInput1.setAttribute('name', 'dwFileType');
		crtInput1.setAttribute('value', pStrFileType);
	
		crtForm.appendChild(crtInput1);
		
		crtForm.submit();
	} else {
		// print
		var win = window.open();
		self.focus();
		win.document.open();
		
		win.document.write("<html><head>");
		win.document.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"/common/css/submains_v2.css?ver=240325\" />");
		win.document.write("</head><body>");                                                     
		win.document.write("<div align=\"center\">"+ pStrFileName + "</div><div align=\"left\">" + labelString + "</div><br/>");
		win.document.write($(".cont_table").html().replace("<table ", "<table style=\"border-right:1px solid #DADADA; border-left:1px solid #DADADA; border-bottom:1px solid #DADADA;\" "));
		win.document.write("</body></html>");
		
		win.document.close();
		win.print();
		win.close();
	}
}

/**
 * 개인정보 처리방침 변경 안내 
 * @since  2016-03-17
 * @modify 2016-03-17
 */
function fn_preOpenHelp( pstrVal )
{
	var strUrl = "";
	var pStrName = "";
  
	if( pstrVal == "1" )
	{
		pStrName = "20151108";
	}
	else if( pstrVal == "2" )
	{
		pStrName = "20130103";  
	}
	else if( pstrVal == "3" )
	{
		pStrName = "20170313";  
	}
	else if( pstrVal == "4" )
	{
		pStrName = "20180307";  
	}
	else if( pstrVal == "5" )
	{
		pStrName = "20200517";  
	}
	else if( pstrVal == "6" )
	{
		pStrName = "20201231";  
	}
	else if( pstrVal == "7" )
	{
		pStrName = "20210630";  
	}
	else if( pstrVal == "8" )
	{
		pStrName = "20211109";  
	}
	else if( pstrVal == "9" )
	{
		pStrName = "20221231";  
	}
	else if( pstrVal == "10" ){
		pStrName = "20231116";
	}
	else if( pstrVal == "11" ){
		pStrName = "20240101";
	}else if( pstrVal == "12" ){
		pStrName = "20240430";
	}else if( pstrVal == "13" ){
		pStrName = "20241231";
	}else if( pstrVal == "14" ){
		pStrName = "20260129";
	}
	
	strUrl = "/bizcommon/popup/popup_search.xhtml";
	
	strUrl = strUrl + "?pName=" + pStrName;
	
	// 화면 중앙에서 오픈되도록 위치 지정
	//210916_ 수정 : 팝업 width 수정.
	window.open( strUrl, 'PrivacyPolicy', "toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=no,width=1200,height=800");
	
}
