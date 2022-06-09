$(function() {
     $("form>button[type='submit']").click(function(){
       if (confirm("Ви впевнені у своїх діях?") == true) {
         return true;
       } else {
         return false;
       }
     });
  });