function loginToSignup() {
  $('#loginClose').click();
  $('#signup').click();
  console.log('signup.click is finished')
  return 0;
}

$('#signupModal').on('hidden', function() {
  console.log('modal hide.')
  $(this).data('modal').$element.removeData();
})

function loginCheck(url, csrf_token){
  var emailAddress = $("#login-email").val().trim()
  if(emailAddress == '') {
    alert("아이디를 입력하십시오.");
    return false;
  }
  var password = $("#login-password").val().trim()
  if(password == '') {
    alert("비밀번호를 입력하십시오.");
    return false;
  }
  $.ajax({
    type: "POST",
    // todo --> url --> get from parameter
    url: url,
    data: {'email': emailAddress, 'password': password,'csrfmiddlewaretoken': csrf_token},  // 서버로 데이터 전송시 옵션
    dataType: "json",
    success: function(response){
      if(response.result != 'ok') {
        alert(response.msg);
      }
      else {
        console.log("ok");
        console.log("success login");
        location.reload();
      }
    }
  })
}

function showPassword(id){
  var password = document.getElementById(id);
  password.type = "text";
}

function hidePassword(id){
  var password = document.getElementById(id);
  password.type = "password";
}

function checkEmail(url, csrf_token){
  var emailAddress = $("#emailaddress").val().trim()
  if(emailAddress == '') {
    alert("이메일을 입력하십시오.");
    return false;
  }
  else {
    $.ajax({
      type: "POST",
      url: url,
      data: {'email': emailAddress, 'csrfmiddlewaretoken': csrf_token},  // 서버로 데이터 전송시 옵션
      dataType: "json", 
      success: function(response){ 
        if (response.result != 'ok') {
          alert(response.msg);
        } else {
          console.log("ok");
          $("#email_guide").css("display", "block");
          $("#email_guide").text('인증메일이 ' + emailAddress + ' (으)로 전송되었습니다.받으신 이메일을 열어 링크를 클릭하시면 인증이 완료됩니다.');
          
        }
      },
      error: function(request, status, error){
        alert("오류가 발생했습니다. 다시 시도해 주십시오.");
        location.reload();
      },
    });
  }
}
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

  if(pw.length < 8 || pw.length > 12){
    $("#pw_txt1").removeClass('good')
    $("#pw_txt1").addClass('bad')
  }
  else{
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
  // Todo --> 조건 에외 체크
  if(pw.search(/^(?=.*?[A-Za-z])(?=.*?[0-9])/) == -1){
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

function frmCheck(url, csrf_token){
  console.log('frmCheck invoked')
  let flag = true;
  $.ajax({
    type: "POST",
    url: url, 
    data: {'email':  $("#emailaddress").val().trim(), 'csrfmiddlewaretoken': csrf_token},
    async: false,
    success: function(confirm){ 
      if(typeof(confirm) === 'string' && (confirm != 0 && confirm != 1)){
        alert(confirm)
        flag = false;
        return flag;
      }
      else if(confirm == 0) {
        alert("이메일 인증을 완료한 뒤 다시 시도해 주십시오.");
        flag = false;
        return flag;
      }
      else{
        console.log('Email validation passed');
      }
    },
    error: function(request, status, error){
      alert("오류가 발생했습니다. 다시 시도해 주십시오.");
      console.log(error)
      // location.reload();
    },
  });
  if(flag == false){
    return flag;
  }
  var pw = $("#signup-password-f").val();
  if((pw.length >= 8 && pw.length <= 12) && pw.search(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/) != -1){
    console.log('valid password');
    if($("#signup-password-f").val() == $("#signup-password-s").val()){
      console.log("valid conf-password");
    }
    else{
      alert("비밀번호 확인란을 정확히 입력해주세요.")
      flag = false;
      return flag;
    }
  }
  else{
    alert("비밀번호를 정확히 입력해주세요.");
    flag = false;
    return flag;
  }
  if(document.getElementById('termCheckBox').checked){
    console.log('term box is checked')
  }
  else{
    alert("개인정보 이용약관에 동의해주세요.");
    flag = false;
    return flag;
  }
  alert($("#emailaddress").val().trim() + "님의 회원가입이 완료 되었습니다.\n로그인페이지로 이동하여 회원접속 후 이용가능합니다.");
  $("#regist_frm").submit();
}
