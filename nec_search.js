/**
 * Include 통합검색 공통함수 - 외부 스크립트파일
 * @identify search.js
 * @since 	 2014-04-14
 * Copyright (C)2014 by Libeka Co. Ltd. All right reserved.
 */

/** 공통변수 선언 */

/**
 * onLoad 이벤트 함수
 * @since  2014-04-10
 * @modify 2014-04-11 
 */
$(document).ready(function()
{
	//$('input, textarea').placeholder();
	//$("#searchKeyword").attr('placeholder','정확한 후보자 명을 두 글자 이상 입력하세요.');
	
	//$("#searchKeywrod").val("${searchKeyword}");
	//$("#searchKind").val("${searchKind}");
});

/**
 * 입력된 값 유무 체크 함수
 * @since  2014-04-10
 * @modify 2014-04-10
 */
function fn_iptSearchInput( pstrValue )
{	
	if( pstrValue == 'y' ) 
	{
		$("#searchKeyword").val('');
		return;
	}
	else
	{
		if( $("#searchKeyword").val() == "" )
		{	
			//fn_changeGuide();			
			$("#searchKeyword").removeClass( "noimg" );
		}
		else
		{
			$("#searchKeyword").addClass( "noimg" );
		}
	}	
}

/**
 * 문자열이 특수문자를 포함하고 있는지 여부 체크 함수
 * @since  2014-04-14
 * @modify 2014-04-14
 * @param  : pstrValue : 체크할 문자열 ( 예 : "가나다" ) 
 * @return : 특수문자가 있을 경우 = true
 *           특수문자가 없을 경우 = false
 */
function fn_isSpecialChar( pstrValue ) 
{
	var strSpecialChar = "~!@\#$%<>^&*\()\-=+_\'";

	for( var intI = 0; intI < pstrValue.length; intI++) 
	{
		if( strSpecialChar.indexOf( String( pstrValue ).substring( intI, intI + 1 ).toUpperCase() ) > -1 ) 
		{
			return true;
		}
	}

	return false;
}

/**
 * 문자열이 한글로만 구성되어 있는지 체크 함수
 * @since  2014-04-14
 * @modify 2014-04-14
 * @param  : pstrValue : 체크할 문자열 
 * @return : 한글이 아닌 글자가 하나라도 있는 경우 = true
 *           한글만 있는경우 = false
 */   
function fn_isKor( pstrValue )
{
	var i;
		
	for( i = 0 ; i < pstrValue.length ; i++ )
	{
		if( !( ( pstrValue.charCodeAt( i ) > 0x3130 && pstrValue.charCodeAt( i ) < 0x318F ) 
				 || ( pstrValue.charCodeAt( i ) >= 0xAC00 && pstrValue.charCodeAt( i ) <= 0xD7A3 ) ) )
		{
			return true;
		}
	}
	
	return false;
}

/**
 * 문자열이 영어가 존재하는지 체크 함수
 * @since  2014-07-11
 * @modify 2014-04-11
 * @param  : pstrValue : 체크할 문자열 
 * @return : 영문이 하나라도 있는 경우 = true
 *           영문이 아니면 = false
 */   
function fn_isEng( pstrValue )
{
	var eng_check = /^[A-za-z]/g;
	if( eng_check.test( pstrValue ) )
	{		
		return true;
	}
	else
	{
		return false;
	}
}
/**
 * NULL 여부 체크 함수
 * @since  2014-04-14
 * @modify 2014-04-14
 * @param  : pstrValue : 체크할 문자열 
 * @return : NULL 이면 true
 *           NULL 이 아니면 = false
 */  
function fn_isNull( pstrValue )
{
    if( new String( pstrValue ).valueOf() == "undefined") return true;
    
    if( pstrValue == null ) return true;
    
    var v_chkStr = ( new String( pstrValue ) ).replace(/^\s+|\s+$/g, '');

    if( v_chkStr == null ) return true;
  
    if( v_chkStr.toString().length == 0 ) return true;

    return false;
}

/**
 * 통합검색 안내글 변경 함수
 * @since  2014-04-10
 * @modify 2014-04-10
 */
function fn_changeGuide() 
{	
	// searchKind 종류에 따라 안내 글 변경
	switch( $("#searchKind").val() )
	{
		case "person" :		// 인명 검색	  		
			//$("#searchKeyword").attr('placeholder','정확한 후보자 명을 두 글자 이상 입력하세요.');
	  		break;
	  		
		case "vote" :	 	// 읍면동 검색
			//$("#searchKeyword").attr('placeholder','검색하실 읍면동명을 두 글자 이상 입력하세요.');
	  		break;

		case "menu" :	 	// 메뉴 검색
			//$("#searchKeyword").attr('placeholder','검색하실 메뉴명을 입력하세요.');
	  		break;  		
	  		
		default:			
			break;
	}	
}

/**
 * 통합검색 함수
 * @since  2014-03-24
 * @modify 2014-04-10 
 */
function fn_commonSearch( pstrValue )
{	
	//alert($("#searchKeyword").val());
	
	/*
	////////////////////////////////////////////
	////// 조건별 읍면동검색 결과 탭 사용설정 //////////         
	////////////////////////////////////////////
	if( $("#searchKind").val() == "vote" )
	{
		if( pstrValue != "TAB" )
		{
			$("#voteSearchType").val('2');
		}
	}
	////////////////////////////////////////////
	////// 조건별 읍면동검색 결과 탭 사용설정 //////////         
	////////////////////////////////////////////	
	
	if( pstrValue != "PAGE" )
	{
		$("#pageIndex").val( 1 );
		$("#firstIndex").val( 0 );		
	}
	*/

	
	if($(".searchBtn").css("pointer-events")=='none'){
		return;
	}
	if(typeof($("#searchKeyword").data("placeholder-value")) != 'undefined' && $.trim($("#searchKeyword").data("placeholder-value")).length>0 && $.trim($("#searchKeyword").data("placeholder-value")) == $("#searchKeyword").val()){
		alert("검색하실 내용을 입력해주세요.");
		return;
		$("#searchKeyword").focus();
	}

	// 유효성 여부 체크
	if( fn_isValidateCheck( $("#searchKeyword").val(), $("#searchKind").val() ) == true )
	{
		$("#searchKeyword").focus();
		return; 
	}
	/*
	if( fn_isNull( $("#searchKeyword").val() ) == true )	
	{		
		alert( "검색하실 내용을 입력해주세요." );
		$("#searchKeyword").focus();
		
		return; 
	}
	else if( $("#searchKind").val() != "menu" && $("#searchKeyword").val().length < 2 ) 
	{
		alert("검색어는 두 글자 이상 입력해 주세요.");
		$("#searchKeyword").focus();
		
		return;
	}
	else if( fn_isKor( $("#searchKeyword").val() ) == true )
	{
		alert("한글만 입력하세요.");
		$("#searchKeyword").focus();
		
		return ;
	}
	else if( fn_isSpecialChar( $("#searchKeyword").val() ) == true )
	{
		alert("특수문자는 사용하실수 없습니다.");
		
		return;
	}
	*/
	
	/*
	switch( $("#searchKind").val() )
	{
		case "person" :		// 인명 검색	  		
			//document.location.href ="main_searchPersonBase.xhtml?electionId=" + $("#electionId").val() + "&searchKeyword="+encodeURIComponent( $("#searchKeyword").val() );
			document.location.href = "/search/searchPersonBase.xhtml?electionId=" + $("#electionId").val() + "&searchKeyword=" + encodeURIComponent( $("#searchKeyword").val() ) + "&pageIndex=" + $("#pageIndex").val() + "&firstIndex=" + $("#firstIndex").val() + "&recordCountPerPage=" + $("#recordCountPerPage").val();
	  		break;
	  		
		case "vote" :	 	// 읍면동 검색
			document.location.href = "/search/searchVotePlace.xhtml?electionId=" + $("#electionId").val() + "&searchKeyword=" + encodeURIComponent( $("#searchKeyword").val() ) + "&voteSearchType=" + $("#voteSearchType").val();
	  		break;

		case "menu" :	 	// 메뉴 검색
			document.location.href = "/search/searchMenu.xhtml?electionId=" + $("#electionId").val() + "&searchKeyword=" + encodeURIComponent( $("#searchKeyword").val() );
	  		break;  		
	  		
		default:			
			break;
	}
	*/
	
	/*document.location.href = "/search/searchCandidate.xhtml?electionId=" + $("#electionId").val() + "&searchKeyword=" + encodeURIComponent( $("#searchKeyword").val() ) + "&pageIndex=" + $("#pageIndex").val() + "&firstIndex=" + $("#firstIndex").val() + "&recordCountPerPage=" + $("#recordCountPerPage").val();*/
	
	
	
	$(".searchBtn").css("pointer-events","none").css("cursor","default");
	var searchKeyword=$("#searchKeyword").val();
	/*$("#searchKeyword").val('');*/
	document.location.href = "/search/searchCandidate.xhtml?searchKeyword=" + encodeURIComponent(searchKeyword);
}

/**
 * 통합검색 화면이동
 * @since  2016-10-17
 * @modify 2016-10-17
 */
function fn_goSearch(){
	document.location.href = "/search/searchCandidate.xhtml?searchKeyword=false";
}


function addInputHandler(conditions){
    var $input = conditions.input;
    var dataType = conditions.dataType;
    var eventType = conditions.eventType;
    if ((!$input) || (!dataType)) {
        throw {error:"NotEnoughArguments", errorMsg:"required argument is missing " +((!$input)?" target input element":" dataType")}
        return;
    }
    if ($input[0].tagName != "INPUT") {
        throw {error:"IlregalTargetElement", errorMsg:"target element is not input"};
        return;
    }
    if ((!eventType)) {
        eventType = "keyup";
    }
    var handlerFunc = conditions.handler;
    if ((!handlerFunc)) {
        handlerFunc = function(event){
            $("#divKeyCode").empty().html("<span> event key code = "+event.keyCode+"</span>");
            var regEx = null;
            if (dataType == "N") {
                regEx = /[^0-9]/gi;
            } else if (dataType == "AP") {
                regEx = /[^a-zA-Z]/gi;
            }else if (dataType == "AN") {
                regEx = /[^a-zA-Z0-9]/gi;
            }else if (dataType == "HA") {
                //regEx = /[a-z0-9]/gi;
            	regEx = /[^ㄱ-힣]/gi;
            }else if (dataType == "HANUM") {
                    //regEx = /[a-z0-9]/gi;
                	regEx = /[^ㄱ-힣0-9\-\s]/gi;
            } else if (dataType == "APB") {
                regEx = /[^a-zA-Z\s]/gi;
            }else if (dataType == "EM") {
                regEx = /[^a-zA-Z0-9.@]/gi;
            }else if (dataType == "EEM") {
                regEx = /[^a-zA-Z0-9.@_-]/gi;
            } else if (dataType == "ADR") {
                regEx = /[^a-zA-Z0-9,.\-#/"&Φ_:'~`!@%=;<>ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ\^\[\]\$\(\)\|\*\+\?\{\}\\\s]/gi;
            }else if (dataType == "RESN") {
            	regEx = /[^\u1100-\u11FF\uAC00-\uD7AF\u3130-\u318F\u0030-\u0039,.\-#/"&Φ_:'~`!@%=;<>ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ\^\[\]\$\(\)\|\*\+\?\{\}\\\u0020]/gi;
            }
            else{
                throw {error:"IlregalDataType", errorMsg:"dataType("+dataType+") is incorrect"};
            }
            remainOnlyTargetValue(regEx, $input,event);
            //return true;
        };  // end of handlerFunc
    } // end of if to check handlerFunc
    $input.on(eventType,handlerFunc);

    if (conditions.maxlength) {
        $input.attr("maxlength",conditions.maxlength);
    }

}

function remainOnlyTargetValue(regEx, $input,event) {
    if ((!(event.keyCode >=34 && event.keyCode<=40)) && event.keyCode != 16) {
        var inputVal = $input.val();
        if (regEx.test(inputVal)) {
            $input.val(inputVal.replace(regEx,''));
        }
    }
}





/**
 * 통합검색 함수(배너방식)
 * @since  2014-07-08
 * @modify 2014-07-08
 */
function fn_commonSearchBanner( pstrValue )
{	
	// 읍면동 검색으로 기본 설정
	$("#searchKind").val("vote");
	
	////////////////////////////////////////////
	////// 조건별 읍면동검색 결과 탭 사용설정 //////////         
	////////////////////////////////////////////
	if( $("#searchKind").val() == "vote" )
	{
		if( pstrValue != "TAB" )
		{
			$("#voteSearchType").val('2');
		}
	}
	////////////////////////////////////////////
	////// 조건별 읍면동검색 결과 탭 사용설정 //////////         
	////////////////////////////////////////////
	
	// 유효성 여부 체크
	if( fn_isValidateCheck( $("#searchKeyword").val(), $("#searchKind").val() ) == true )
		return;
	
	// 읍면동 검색
	document.location.href = "/search/banner/searchBannerVotePlace.xhtml?electionId=" + $("#electionId").val() + "&searchKeyword=" + encodeURIComponent( $("#searchKeyword").val() ) + "&voteSearchType=" + $("#voteSearchType").val();
}

/**
 * 유효성 여부 체크 함수
 * @since  2014-05-28
 * @modify 2014-05-28
 */
function fn_isValidateCheck( pstrValue1, pstrValue2 )
{	
	var blnCheck	= false;
	var infoMsg		= "";
	var is_opera 	= navigator.userAgent.toLowerCase().indexOf("opera") > -1;
	var is_chrome 	= navigator.userAgent.toLowerCase().indexOf("chrome") > -1;
	
	if( fn_isNull( pstrValue1 ) == true )	
	{		
		infoMsg		= "검색하실 내용을 입력해주세요.";
		blnCheck	= true;
	}
	else if( pstrValue2 != "menu" && pstrValue1.length < 2 ) 
	{
		infoMsg		= "검색어는 두 글자 이상 입력해 주세요.";
		blnCheck	= true;
	}
	else if( fn_isKor( pstrValue1 ) == true )
	{
		infoMsg		= "한글만 입력하세요.";
		blnCheck	= true;
	}
	else if( fn_isEng( pstrValue1 ) == true )
	{
		infoMsg		= "한글로 입력해주세요.";
		blnCheck	= true;
	}
	else if( fn_isSpecialChar( pstrValue1 ) == true )
	{		
		infoMsg		= "특수문자는 사용하실수 없습니다.";
		blnCheck	= true;
	}
	
	if( blnCheck == true )
	{
		alert( infoMsg );
		
		if( is_opera || is_chrome )
		{
			
		}
		else
		{
			$("#searchKeyword").focus();
		}
	}	
	
	return blnCheck;
}

/**
 * 읍면동별 후보자 보기 팝업
 * @since  2014-05-08
 * @modify 2014-05-08
 */
function fn_showCandidate( pstrEmdId ) 
{
	document.location.href = "/search/searchEmdCandidate.xhtml?electionId=${electionId}&emdId=" + pstrEmdId + "&searchKeyword=" + encodeURIComponent("${searchKeyword}");
}

/**
 * 후보자 정보공개 팝업 - href="javascript:fn_showCandidatePromise('${electionId}','${item.HUBOID}');"
 * @since  2014-05-12
 * @modify 2014-05-12
 */
function fn_showCandidateInfo( electionId, huboId )
{
	var is_safari = false;
	
	if( ( navigator.userAgent.toLowerCase().split("safari").length + navigator.userAgent.toLowerCase().split("chrome").length) > 3 )
	{
		is_safari = false;
	}
	else
	{
		is_safari = true;
	}
	
	var is_msie 	= navigator.userAgent.toLowerCase().indexOf("msie") > -1;
	var is_firefox 	= navigator.userAgent.indexOf("Firefox") > -1;
	var is_opera 	= navigator.userAgent.toLowerCase().indexOf("opera") > -1;
	var is_chrome	= navigator.userAgent.toLowerCase().indexOf("chrome") > -1;

	if( is_msie || is_firefox || is_opera || is_safari || is_chrome )
	{
		//var url	= '${ctx}/electioninfo/candidate_detail_basicInfo.xhtml?electionId=' + electionId + '&huboId=' + huboId;
		//var url	= '/electioninfo/candidate_detail_basicInfo.xhtml?electionId=' + electionId + '&huboId=' + huboId;
		var url	= '/electioninfo/candidate_detail_info.xhtml?electionId=' + electionId + '&huboId=' + huboId;
		
		window.open(url, 'showCandidateInfo', "toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no, width=1020, height=760, left=0, top=0");
		
		return;
	}
	else
	{
		alert("죄송합니다. 현재 후보자정보공개현황 팝업페이지는 마이크로 소프트 인터넷 익스플로러나 파이어폭스, 사파리, 오페라, 크롬에서 확인하실수 있습니다.");
		
		return;
	}
}

/**
 * 후보자 공약 팝업 - href="javascript:fn_showCandidatePromise('${item.CUID}');"
 * @since  2014-05-12
 * @modify 2014-05-12
 */
function fn_showCandidatePromise( cuid )
{
	var documentURI = 'http://party.nec.go.kr/people/popup/publicpledgepolicy/read.xhtml?candidateNo=' + cuid;
	
	window.open(documentURI, "showCandidatePromise", "scrollbars=yes,resizable=yes, width=687, height=550, left=0, top=0");
}