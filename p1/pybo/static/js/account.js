
function showPassword(id){
  var password = document.getElementById(id);
  password.type = "text";
}

function hidePassword(id){
  var password = document.getElementById(id);
  password.type = "password";
}

function checkEmail(csrf_token){
    if($("#emailaddress").val().trim() == '') {
      alert("이메일을 입력하십시오.");
      return false;
    }else {
      $.ajax({
        type: "POST",
        url: "account/check_email",
        data: {'email': $("#emailaddress").val().trim(), 'csrfmiddlewaretoken': csrf_token},  // 서버로 데이터 전송시 옵션
        dataType: "json", 
        success: function(response){ 
          if (response.result != 'ok') {
            alert(response.msg);
          } else {
            console.log("ok");
            // show alert div whether sended
          }
        },
        error: function(request, status, error){
          alert("오류가 발생했습니다. 다시 시도해 주십시오.");
          location.reload();
        },
      });
    }
}
// 이메일 인증 확인(완료 버튼)
$("#completeButton").click(function(){
  $.ajax({
    type: "GET",
    url: "{% url 'check_certification' %}", 
    data: {'email':  $("#emailaddress").val().trim()},
    success: function(confirm){ 
      if(confirm == '0') {
        alert("이메일 인증을 완료한 뒤 다시 시도해 주십시오.");
        // show alert div instead of errormodal
      }else{
        console.log('Email validation passed');
      }
    },
    error: function(request, status, error){
      alert("오류가 발생했습니다. 다시 시도해 주십시오.");
      location.reload();
    },
  });
  return false;
});
$("#signup-password-f").click(function(){
  console.log("password input clicked");
  $("#password_guide").css("display", "block")
});

$("#signup-password-s").click(function(){
  console.log("confirm password input clicked");
  $("#confirm_guide").css("display", "block")
});

$(".pwcheck").on('input', function(){
  console.log($(this).val());

  // 영문/숫자/특수문자 2개 이상조합 8-12 자리
  var pw = $("#signup-password-f").val();
  var num = pw.search(/[0-9]/g);
  var eng = pw.search(/[a-z]/ig);
  var spe = pw.search(/[`~!@@#$%^&*|₩₩₩'₩";:₩/?]/gi);
  var test = pw.search(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/);
  console.log('test=',test)
  console.log('pw.search(/\s/) != -1',pw.search(/\s/) != -1);
  console.log('num < 0 && eng < 0',num < 0 && eng < 0);
  console.log('eng < 0 && spe < 0',eng < 0 && spe < 0);
  console.log('spe < 0 && num < 0',spe < 0 && num < 0);
  if(pw.length < 8 || pw.length > 12){
    $("#pw_txt1").removeClass('good')
    $("#pw_txt1").addClass('bad')
  }else{
    $("#pw_txt1").removeClass('bad')
    $("#pw_txt1").addClass('good')
  }
  // logical operator 에러
  // if(pw.search(/\s/) != -1 && (num < 0 && eng < 0) || (eng < 0 && spe < 0) || (spe < 0 && num < 0) ){
  //   console.log("invoked(True)")
  //   $("#pw_txt2").removeClass('good')
  //   $("#pw_txt2").addClass('bad')
  // }else{
  //   console.log("else invoked(False)")
  //   $("#pw_txt2").removeClass('bad')
  //   $("#pw_txt2").addClass('good')
  // }
  if(pw.search(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/) == -1){
    $("#pw_txt2").removeClass('good')
    $("#pw_txt2").addClass('bad')
  }
  else{
    $("#pw_txt2").removeClass('bad')
    $("#pw_txt2").addClass('good')
  }
  if($("#signup-password-f").val()!=$("#signup-password-s").val() || $("#signup-password-s").val().trim()==""){
    $("#confirm_txt").removeClass('good')
    $("#confirm_txt").addClass('bad')
  }else{
    $("#confirm_txt").removeClass('bad')
    $("#confirm_txt").addClass('good')
  }
});

function frmCheck(){
  let flag = true;

  $('input').each(function(){
    if ($(this).val() == '') {
      alert("필수 정보를 입력하십시오.")
      flag = false;
      $(this).focus();
    }
  })

  if(flag) $("#regist_frm").submit();
  else return flag;
}